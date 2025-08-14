
data = ["Apple", "Banana", "Cherry"]  # or data = "Just a string"

if isinstance(data, list) and all(isinstance(x, str) for x in data):
    st.write("Choose an option:")
    for item in data:
        if st.button(item):
            st.write(f"You clicked: {item}")

elif isinstance(data, str):
    st.write(f"Received a single string: {data}")
    # Do something else here
else:
    st.error("Unexpected data format.")
