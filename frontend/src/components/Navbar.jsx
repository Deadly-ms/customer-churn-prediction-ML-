function Navbar() {
    return (
        <nav
            style={{
                background: "rgba(255, 255, 255, 0.8)",
                backdropFilter: "blur(20px)",
                WebkitBackdropFilter: "blur(20px)",
                color: "#1d1d1f",
                padding: "18px 32px",
                textAlign: "center",
                fontSize: "19px",
                fontWeight: 600,
                letterSpacing: "-0.02em",
                borderBottom: "1px solid rgba(0, 0, 0, 0.08)",
                fontFamily:
                    "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif",
                position: "sticky",
                top: 0,
                zIndex: 10,
            }}
        >
            Customer Churn Prediction
        </nav>
    );
}

export default Navbar;