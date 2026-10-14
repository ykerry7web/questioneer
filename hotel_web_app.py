import streamlit as st

st.set_page_config(page_title="Hotel Room Bookings", page_icon="🏨", layout="centered")
st.title("🏨 Hotel Room Bookings")
st.write("Book a room, view bookings, or search by guest name.")

# This keeps bookings while the current app session is running.
if "rooms" not in st.session_state:
    st.session_state.rooms = []

tab_book, tab_view, tab_find = st.tabs(["Book a room", "View bookings", "Find a booking"])

with tab_book:
    st.subheader("Book a room")
    with st.form("booking_form"):
        name = st.text_input("Guest name")
        room_number = st.number_input("Room number", min_value=1, step=1)
        submitted = st.form_submit_button("Book room", use_container_width=True)
    if submitted:
        if not name.strip():
            st.error("Please enter the guest's name.")
        else:
            st.session_state.rooms.append({"name": name.strip(), "number": int(room_number)})
            st.success("Room booked successfully.")

with tab_view:
    st.subheader("Current bookings")
    if not st.session_state.rooms:
        st.info("No rooms booked yet.")
    else:
        st.dataframe(
            [{"Guest name": booking["name"], "Room number": booking["number"]}
             for booking in st.session_state.rooms],
            hide_index=True,
            use_container_width=True,
        )

with tab_find:
    st.subheader("Find a booking")
    search_name = st.text_input("Enter a guest name", key="search_name")
    if st.button("Search", use_container_width=True):
        matches = [booking for booking in st.session_state.rooms
                   if booking["name"].casefold() == search_name.strip().casefold()]
        if matches:
            for booking in matches:
                st.success(f"{booking['name']} — room {booking['number']}")
        else:
            st.warning("No booking found for that name.")

st.caption("Prototype: bookings are kept temporarily in the current browser session.")
