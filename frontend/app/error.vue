<template>
  <div class="bg-surface font-body-md text-on-surface min-h-screen flex items-center justify-center p-4">
    <!-- 404 Page (Isolated Context) -->
    <section v-if="error?.statusCode === 404" class="flex flex-col items-center justify-center py-24 px-12 bg-surface-container-lowest/50 rounded-3xl border border-outline-variant/20 max-w-3xl w-full" id="not-found">
      <div class="relative text-center w-full">
        <h1 class="font-display text-[120px] md:text-[160px] leading-none text-outline-variant opacity-20 pointer-events-none select-none">404</h1>
        <div class="absolute inset-0 flex flex-col items-center justify-center mt-8">
          <h2 class="font-headline-lg text-headline-lg text-on-surface mb-2">Page not found</h2>
          <p class="font-body-md text-body-md text-on-surface-variant mb-8">The analytical path you followed doesn't exist anymore.</p>
          <Button @click="handleError" class="bg-primary !text-white px-8 py-6 h-auto rounded-lg font-label-md text-label-md hover:bg-primary/90 transition-all flex items-center gap-2 shadow-md">
            <span class="material-symbols-outlined">dashboard</span>
            Go to Dashboard
          </Button>
        </div>
      </div>
    </section>

    <!-- General Error -->
    <section v-else class="flex flex-col items-center justify-center py-24 px-12 bg-surface-container-lowest/50 rounded-3xl border border-error/20 max-w-3xl w-full">
      <div class="relative text-center w-full">
        <h1 class="font-display text-[120px] md:text-[160px] leading-none text-error opacity-10 pointer-events-none select-none">{{ error?.statusCode || 'Error' }}</h1>
        <div class="absolute inset-0 flex flex-col items-center justify-center mt-8">
          <h2 class="font-headline-lg text-headline-lg text-error mb-2">An error occurred</h2>
          <p class="font-body-md text-body-md text-on-surface-variant mb-8">{{ error?.message || "Something went wrong during the analysis." }}</p>
          <Button @click="handleError" variant="outline" class="border-2 border-error text-error px-8 py-6 h-auto rounded-lg font-label-md text-label-md hover:bg-error hover:text-white transition-all flex items-center gap-2">
            <span class="material-symbols-outlined">home</span>
            Back to Home
          </Button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Button } from '~/components/ui/button/index'
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})

const handleError = () => clearError({ redirect: '/dashboard' })
</script>
