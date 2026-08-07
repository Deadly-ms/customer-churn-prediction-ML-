import { useState } from "react";

import Navbar from "./components/Navbar";
import CustomerForm from "./components/CustomerForm";
import PredictionCard from "./components/PredictionCard";

import "./App.css";

function App() {

    const [prediction, setPrediction] = useState(null);

    return (

        <div>

            <Navbar />

            <div
                style={{
                    width: "500px",
                    margin: "30px auto"
                }}
            >
                <CustomerForm
                    onPrediction={setPrediction}
                />

                <PredictionCard
                    result={prediction}
                />
            </div>

        </div>

    );

}

export default App;