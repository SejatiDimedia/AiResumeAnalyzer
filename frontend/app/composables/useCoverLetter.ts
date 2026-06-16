import { ref } from 'vue'
import { useAuth } from '~/composables/useAuth'

export const useCoverLetter = () => {
  const { apiFetch } = useAuth()
  const coverLetter = ref<string>('')
  const isGenerating = ref(false)
  const error = ref<string | null>(null)

  const generateCoverLetter = async (analysisId: string): Promise<boolean> => {
    isGenerating.value = true
    error.value = null
    coverLetter.value = ''

    try {
      const result = await apiFetch<{ cover_letter: string }>(
        `/analysis/${analysisId}/cover-letter`,
        { method: 'POST' }
      )
      if (result && result.cover_letter) {
        coverLetter.value = result.cover_letter
        return true
      }
      return false
    } catch (e: any) {
      error.value = e?.data?.detail || 'Failed to generate cover letter. Please try again.'
      return false
    } finally {
      isGenerating.value = false
    }
  }

  return { coverLetter, isGenerating, error, generateCoverLetter }
}
