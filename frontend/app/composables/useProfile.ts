import { useAuth } from '~/composables/useAuth'

export const useProfile = () => {
  const { apiFetch } = useAuth()
  
  const fetchSavedResume = async () => {
    try {
      const response: any = await apiFetch('/profile/resume')
      return response
    } catch (error) {
      console.error(error)
      return { has_profile: false, resume_text: null }
    }
  }

  const uploadSavedResume = async (file: File) => {
    try {
      const formData = new FormData()
      formData.append('file', file)
      
      const response: any = await apiFetch('/profile/resume', {
        method: 'POST',
        body: formData
      })
      
      return response
    } catch (error: any) {
      console.error(error)
      throw new Error(error.response?._data?.detail || 'Failed to upload profile')
    }
  }

  return {
    fetchSavedResume,
    uploadSavedResume
  }
}
