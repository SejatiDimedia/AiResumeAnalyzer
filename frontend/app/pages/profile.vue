<template>
  <div class="flex justify-center pt-8">
    <Card class="bg-white w-full max-w-[720px] rounded-xl border-outline-variant/20 shadow-[0_1px_3px_rgba(0,0,0,0.08)] overflow-hidden relative border-0 ring-1 ring-outline-variant/20">
      
      <div class="p-8 space-y-8">
        <div class="flex flex-col gap-1">
          <h1 class="font-headline-lg text-headline-lg text-on-surface tracking-tight">My Profile</h1>
          <p class="text-on-surface-variant font-body-md text-body-md">Manage your saved resume profile here.</p>
        </div>

        <div v-if="successMessage" class="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg text-body-md">
          <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-[20px]">check_circle</span>
            <p>{{ successMessage }}</p>
          </div>
        </div>

        <div v-if="errorMessage" class="bg-error/10 border border-error/20 text-error px-4 py-3 rounded-lg text-body-md">
          <div class="flex items-center gap-2">
            <span class="material-symbols-outlined text-[20px]">error</span>
            <p>{{ errorMessage }}</p>
          </div>
        </div>
        
        <section class="space-y-4">
          <div class="flex justify-between items-center">
            <h2 class="font-headline-sm text-headline-sm text-on-surface">Base Resume</h2>
            <div v-if="hasProfile" class="flex items-center gap-1 bg-green-100 px-2 py-1 rounded-full">
              <span class="material-symbols-outlined text-green-700 text-[16px]">check_circle</span>
              <span class="text-green-700 font-label-sm text-label-sm">Saved</span>
            </div>
            <div v-else class="flex items-center gap-1 bg-surface-variant px-2 py-1 rounded-full">
              <span class="material-symbols-outlined text-on-surface-variant text-[16px]">info</span>
              <span class="text-on-surface-variant font-label-sm text-label-sm">Not Saved</span>
            </div>
          </div>
          
          <div v-if="hasProfile" class="p-4 bg-surface-container-low rounded-lg border border-outline-variant">
            <p class="font-body-md text-body-md text-on-surface line-clamp-3">{{ resumePreview }}</p>
          </div>

          <div class="dashed-border group cursor-pointer hover:bg-surface-container-low transition-colors duration-200" @click="triggerFileInput">
            <div class="flex flex-col items-center justify-center py-12 px-6 text-center">
              <span class="material-symbols-outlined text-primary text-[48px] mb-4">cloud_upload</span>
              <p class="font-body-md text-body-md text-on-surface font-semibold" v-if="!selectedFile">Drag & drop your resume here to {{ hasProfile ? 'update' : 'save' }}</p>
              <p class="font-body-md text-body-md text-primary font-semibold" v-else>{{ selectedFile.name }}</p>
              <p class="font-body-sm text-body-sm text-on-surface-variant mt-1" v-if="!selectedFile">Support PDF, DOCX (Max 10MB)</p>
              <Button variant="link" class="mt-4 text-primary font-label-md text-label-md" @click.stop="triggerFileInput">
                {{ selectedFile ? 'Change file' : 'or browse files' }}
              </Button>
              <input type="file" ref="fileInput" class="hidden" accept=".pdf,.docx" @change="onFileChange" />
            </div>
          </div>
        </section>

        <div class="pt-4 flex items-center justify-end gap-4">
          <Button 
            class="bg-primary !text-white px-8 py-4 rounded-lg font-label-md text-label-md shadow-md hover:-translate-y-0.5 hover:shadow-lg transition-all active:scale-95 flex items-center gap-2 h-auto" 
            @click="handleUpload"
            :disabled="!selectedFile || isUploading"
          >
            <span class="material-symbols-outlined text-[18px]" v-if="isUploading">refresh</span>
            {{ isUploading ? 'Saving...' : 'Save Profile' }}
          </Button>
        </div>
      </div>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Card } from '~/components/ui/card/index'
import { Button } from '~/components/ui/button/index'
import { useProfile } from '~/composables/useProfile'

definePageMeta({
  middleware: 'auth'
})

const { fetchSavedResume, uploadSavedResume } = useProfile()

const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)
const isUploading = ref(false)
const hasProfile = ref(false)
const resumePreview = ref('')
const errorMessage = ref('')
const successMessage = ref('')

onMounted(async () => {
  await loadProfile()
})

const loadProfile = async () => {
  const data = await fetchSavedResume()
  if (data.has_profile) {
    hasProfile.value = true
    resumePreview.value = data.resume_text || ''
  }
}

const triggerFileInput = () => {
  fileInput.value?.click()
}

const onFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    selectedFile.value = target.files[0]
    errorMessage.value = ''
    successMessage.value = ''
  }
}

const handleUpload = async () => {
  if (!selectedFile.value) return
  
  isUploading.value = true
  errorMessage.value = ''
  successMessage.value = ''
  
  try {
    const data = await uploadSavedResume(selectedFile.value)
    hasProfile.value = true
    resumePreview.value = data.resume_text || ''
    successMessage.value = 'Profile resume successfully saved!'
    selectedFile.value = null
  } catch (error: any) {
    errorMessage.value = error.message || 'Failed to save profile'
  } finally {
    isUploading.value = false
  }
}
</script>

<style scoped>
.dashed-border {
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='8' ry='8' stroke='%23CBC4D2FF' stroke-width='2' stroke-dasharray='8%2c 8' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
  border-radius: 8px;
}
</style>
