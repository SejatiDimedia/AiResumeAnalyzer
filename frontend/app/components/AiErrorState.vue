<template>
  <section class="max-w-xl mx-auto w-full">
    <div class="bg-error-container/20 border border-error/20 p-12 rounded-xl relative overflow-hidden group">
      
      <!-- Background Icon -->
      <div class="absolute top-0 right-0 p-6 opacity-10 group-hover:opacity-20 transition-opacity">
        <span class="material-symbols-outlined text-[120px] text-error">warning</span>
      </div>
      
      <!-- Content -->
      <div class="flex items-start gap-6 relative z-10">
        <div class="bg-error-container text-error p-2 rounded-lg flex shrink-0">
          <span class="material-symbols-outlined">warning</span>
        </div>
        
        <div class="space-y-2">
          <h2 class="font-headline-sm text-headline-sm text-error font-bold">Analysis failed</h2>
          <p class="font-body-md text-body-md text-on-error-container leading-relaxed">
            We encountered an unexpected error while processing your resume file. This might be due to a complex formatting structure or temporary server load.
          </p>
          
          <div class="pt-6">
            <Button variant="outline" class="border-2 border-error text-error px-6 py-2 h-auto rounded-lg font-label-md text-label-md hover:bg-error hover:text-white transition-all flex items-center gap-2" @click="$emit('retry')">
              <span class="material-symbols-outlined text-[18px]">refresh</span>
              Try Again
            </Button>
          </div>
        </div>
      </div>
      
    </div>
  </section>
</template>

<script setup lang="ts">
import { Button } from '~/components/ui/button/index'

defineEmits(['retry'])
</script>
