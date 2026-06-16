import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<any>(null)
  const isAuthenticated = ref<boolean>(false)

  function setUser(userData: any) {
    user.value = userData
    isAuthenticated.value = !!userData
  }

  function clearUser() {
    user.value = null
    isAuthenticated.value = false
  }

  return {
    user,
    isAuthenticated,
    setUser,
    clearUser
  }
})
