import axios from 'axios'

function createInstance() {
  return axios.create({
    baseURL: 'http://127.0.0.1:8000/api/test'
  });
}

const instance = createInstance();

function fetchTestList() {
  return instance.get('/list');
}

export { fetchTestList };