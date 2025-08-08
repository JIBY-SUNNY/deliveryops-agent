import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const runAgent = async () => {
  const response = await axios.post(`${BASE_URL}/status`);
  return response.data.result;  // <-- only return the inner result
};

