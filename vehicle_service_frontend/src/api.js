import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/";


export const getComponents = () => axios.get(`${API_URL}components/`);
export const getVehicles = () => axios.get(`${API_URL}vehicles/`);
export const getRepairs = () => axios.get(`${API_URL}repairs/`);
