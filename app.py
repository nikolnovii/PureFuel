import streamlit as st
from search_engine import load_products

# Page setup
st.set_page_config(
    page_title="PureFuel",
    page_icon="🥗",
    layout="wide"
)

# Load products
products = load_products("products.json")

# Session state
if "blood_sugar" not in st.session_state:
    st.session_state.blood_sugar = 0

if "energy" not in st.session_state:
    st.session_state.energy = 80

if "money" not in st.session_state:
    st.session_state.money = 0.0

# Sidebar navigation
st.sidebar.title("PureFuel")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Product Search", "Food Insights"]
)

st.title("PureFuel Food Auditor")
st.write("Make more informed food choices.")


# -------------------------
# DASHBOARD
# -------------------------

if page == "Dashboard":

    st.header("Health & Spending Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Blood Sugar Impact",
        st.session_state.blood_sugar
    )

    col2.metric(
        "Energy Level",
        st.session_state.energy
    )

    col3.metric(
        "Total Money Spent",
        f"${st.session_state.money:.2f}"
    )

    st.info(
        "Use Product Search to analyze or update a food product."
    )


# -------------------------
# PRODUCT SEARCH
# -------------------------

elif page == "Product Search":

    st.header("Product Search")

    search_term = st.text_input(
        "Enter a product name or ingredient"
    )

    if search_term:

        results = [
            product for product in products
            if search_term.lower() in product.name.lower()
            or search_term.lower() in str(product.ingredients).lower()
        ]

        if results:

            for product in results:

                st.subheader(product.name)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Sugar Content",
                        f"{product.sugar_content} g"
                    )

                    st.metric(
                        "Processing Level",
                        product.processed_level
                    )

                with col2:
                    st.write("**Ingredients**")
                    st.write(", ".join(product.ingredients))

                    st.write("**Cost**")
                    st.write(f"${product.cost:.2f}")

                # Edit product data
                new_sugar = st.number_input(
                    "Update sugar content",
                    min_value=0.0,
                    value=float(product.sugar_content),
                    step=1.0,
                    key=f"sugar_{product.name}"
                )

                if st.button(
                    "Save Changes",
                    key=f"save_{product.name}"
                ):

                    product.sugar_content = new_sugar

                    # Save change to JSON
                    product.save_to_json("products.json")

                    st.success(
                        f"{product.name} was updated and saved!"
                    )

        else:
            st.warning("No matching products found.")

    st.divider()

    st.subheader("All Available Products")

    for product in products:
        st.write("•", product.name)


# -------------------------
# FOOD INSIGHTS
# -------------------------

elif page == "Food Insights":

    st.header("Food Insights")

    st.write(
        "Look beyond the basic product description "
        "and explore the information behind the label."
    )

    st.divider()

    product_names = [product.name for product in products]

    selected_product = st.selectbox(
        "Choose a product to analyze",
        product_names
    )

    product = next(
        p for p in products
        if p.name == selected_product
    )

    st.subheader(product.name)

    col1, col2 = st.columns(2)

    with col1:

        st.success("Product Information")

        st.metric(
            "Sugar",
            f"{product.sugar_content} g"
        )

        st.write(
            "Review the product information before "
            "making your food choice."
        )

    with col2:

        st.warning("Processing Information")

        st.metric(
            "Processing Level",
            product.processed_level
        )

        st.write(
            "PureFuel looks at ingredients and processing "
            "to provide additional information."
        )

    st.divider()

    st.subheader("Ingredients")

    st.write(", ".join(product.ingredients))

    # Processing-level feedback
    if product.processed_level >= 7:

        st.warning(
            "This product has a high processing level. "
            "The information on the front of the package "
            "may not tell the whole story."
        )

    elif product.processed_level >= 4:

        st.warning(
            "This product has a moderate processing level. "
            "Check the ingredients before making your choice."
        )

    else:

        st.success(
            "This product has a lower processing level "
            "based on the PureFuel data."
        )

    st.divider()

    st.info(
        "PureFuel helps users look beyond simple health claims "
        "and make more informed food choices."
    )