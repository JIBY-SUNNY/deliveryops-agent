import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const runAgent = async () => {
  const response = await axios.post(`${BASE_URL}/run-agent`);
  return response.data;
};
