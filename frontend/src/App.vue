<template>
  <div class="app">
    <h1>Vue + Flask App</h1>
    <button @click="fetchMessage">Get Message from Backend</button>
    <p v-if="message">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>
    <pre v-if="errorDetails" class="error-details">{{ errorDetails }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const message = ref('')
const error = ref('')
const errorDetails = ref('')

const fetchMessage = async () => {
  try {
    error.value = ''
    errorDetails.value = ''
    console.log('Making request to /api/hello')
    const response = await axios({
      method: 'get',
      url: '/api/hello',
      headers: {
        'Content-Type': 'application/json',
      },
      timeout: 5000 // Add timeout to prevent hanging
    })
    console.log('Response received:', response.data)
    message.value = response.data.message
  } catch (err) {
    console.error('Error details:', err)
    error.value = `Error: ${err.message}`
    if (err.response) {
      errorDetails.value = `Status: ${err.response.status}\nData: ${JSON.stringify(err.response.data, null, 2)}`
    } else if (err.code === 'ECONNREFUSED') {
      errorDetails.value = 'Connection refused. Please check if the backend service is running.'
    } else {
      errorDetails.value = `No response received: ${err.message}`
    }
    message.value = ''
  }
}
</script>

<style>
.app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.error {
  color: red;
  margin-top: 1rem;
}

.error-details {
  background-color: #f8f8f8;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  text-align: left;
  white-space: pre-wrap;
  font-family: monospace;
}
</style> 
