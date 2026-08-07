import axios from "axios";

const API = axios.create({
    baseURL: import.meta.env.VITE_API_URL
});

export const predictChurn = async (customerData) => {
    try {
        const response = await API.post("/predict", customerData);
        return response.data;
    } catch (error) {
        console.error("Prediction Error:", error);

        throw error;
    }
};