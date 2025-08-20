import streamlit as st

st.title("Personrotator")

# Startlista
if "persons" not in st.session_state:
    st.session_state.persons = ["Alice", "Bob", "Emelie", "Charlie", "Daniel"]

# Visa aktuell lista
st.subheader("Nuvarande lista")
for i, person in enumerate(st.session_state.persons, start=1):
    st.write(f"{i}. {person}")

# Flytta översta person till sist
if st.button("Välj översta person"):
    if st.session_state.persons:
        st.session_state.persons.append(st.session_state.persons.pop(0))

# Lägg till ny person
new_person = st.text_input("Lägg till person")
if st.button("Lägg till"):
    if new_person.strip():
        st.session_state.persons.append(new_person.strip())

# Ta bort person via nummer
remove_idx = st.number_input("Ta bort person nr", min_value=1, max_value=len(st.session_state.persons), step=1)
if st.button("Ta bort"):
    if 0 < remove_idx <= len(st.session_state.persons):
        st.session_state.persons.pop(remove_idx - 1)
