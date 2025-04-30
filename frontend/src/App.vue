<template>
  <div class="app">
    <h1>Vue + Flask App</h1>
    <button @click="fetchMessage">Get Message from Backend</button>
    <p v-if="message">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>
    <pre v-if="errorDetails" class="error-details">{{ errorDetails }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios, { AxiosError } from 'axios'

const message = ref<string>('')
const error = ref<string>('')
const errorDetails = ref<string>('')

const fetchMessage = async (): Promise<void> => {
  try {
    error.value = ''
    errorDetails.value = ''
    const response = await axios({
      method: 'get',
      url: '/api/hello',
      headers: {
        'Content-Type': 'application/json',
      },
      timeout: 5000
    })
    message.value = response.data.message
  } catch (err) {
    const axiosError = err as AxiosError
    error.value = `Error: ${axiosError.message}`
    if (axiosError.response) {
      errorDetails.value = `Status: ${axiosError.response.status}\nData: ${JSON.stringify(axiosError.response.data, null, 2)}`
    } else {
      errorDetails.value = `No response received: ${axiosError.message}`
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
