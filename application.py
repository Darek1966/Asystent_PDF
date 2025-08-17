import pdfplumber
import streamlit as st
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter


def get_pdf_text(pdf_documents):

    text = ""
    for pdf in pdf_documents:
        with pdfplumber.open(pdf) as pdf_reader:
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1500, chunk_overlap=100, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, input_key="question"
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

    prompt = PromptTemplate.from_template(
        """
        Poniżej znajdują się fragmenty dokumentów i historia rozmowy.
        Odpowiedz na pytanie użytkownika WYŁĄCZNIE na podstawie poniższych fragmentów dokumentów i historii rozmowy.

        Jeśli odpowiedź NIE znajduje się w dokumentach, odpowiedz tylko:
        "Niestety, nie znalazłem odpowiedzi na to pytanie w dostarczonych dokumentach."

        NIE używaj żadnej wiedzy spoza dokumentów.
        NIE zgaduj. NIE twórz odpowiedzi, jeśli nie masz pewności na podstawie dokumentów.

        Historia rozmowy:
        {chat_history}

        Kontekst z dokumentów:
        {context}

        Pytanie użytkownika:
        {question}

        Odpowiedź:
        """
    )

    conversation_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
            "chat_history": lambda x: memory.load_memory_variables({})["chat_history"],
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    st.session_state.memory = memory
    return conversation_chain


def handle_userinput(user_question):
    if not st.session_state.conversation:
        st.error("Najpierw prześlij dokumenty i kliknij przycisk Przetwórz")
        return
    try:
        with st.spinner("Generowanie odpowiedzi..."):
            response = st.session_state.conversation.invoke(user_question)
    except Exception as e:
        st.error(f"Błąd podczas generowania odpowiedzi: {e}")
        return

    st.session_state.memory.save_context({"question": user_question}, {"output": response})

    # Dodaj pytanie i odpowiedź do historii czatu
    st.session_state.chat_history.append({"role": "user", "content": user_question})
    st.session_state.chat_history.append({"role": "ai", "content": response})

    # Wyświetl historię rozmowy jako czat
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def main():
    load_dotenv()
    st.set_page_config(page_title="Zadaj pytanie dotyczące swoich plików PDF")

    # Inicjalizacja stanu sesji
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "memory" not in st.session_state:
        st.session_state.memory = None

    st.header("Asystent Dokumentów PDF")

    user_question = st.chat_input("Zapytać...")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Twoje dokumenty")
        pdf_documents = st.file_uploader(
            "Prześlij swoje dokumenty i kliknij 'Przetwórz'", accept_multiple_files=True
        )

        if st.button("Przetwórz"):
            if not pdf_documents:
                st.error("Prześlij co najmniej jeden dokument")
                return

            with st.spinner("Przetwarzanie"):
                # Get PDF text
                raw_text = get_pdf_text(pdf_documents)
                if not raw_text.strip():
                    st.error("Nie udało się wyodrębnić tekstu z przesłanych plików PDF.")
                    return

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state.chat_history = []

                st.success(f"Dokument {len(pdf_documents)} przetworzono pomyślnie")


if __name__ == "__main__":
    main()
