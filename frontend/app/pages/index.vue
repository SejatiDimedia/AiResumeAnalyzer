<template>
  <div class="text-on-surface bg-surface min-h-screen font-body-md overflow-x-hidden">
    <!-- TopNavBar -->
    <nav class="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-md border-b border-outline-variant/30 shadow-sm transition-shadow duration-300" :class="{ 'shadow-md': scrolled }">
      <div class="flex justify-between items-center px-lg py-sm max-w-[1100px] mx-auto h-16">
        <!-- Brand -->
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-lg">R</span>
          </div>
          <span class="font-headline-md text-headline-md font-bold text-primary">ResumeAI</span>
        </div>
        <!-- Desktop Links -->
        <div class="hidden md:flex items-center gap-xl">
          <NuxtLink class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" to="/dashboard">Dashboard</NuxtLink>
          <NuxtLink class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" to="/analyze">Analysis</NuxtLink>
          <NuxtLink class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" to="/dashboard">History</NuxtLink>
        </div>
        <!-- Actions -->
        <div class="flex items-center gap-md">
          <NuxtLink to="/login" class="hidden sm:block px-md py-sm font-label-md text-label-md text-on-surface-variant hover:bg-surface-container-low transition-all rounded-lg">Sign In</NuxtLink>
          <NuxtLink to="/register">
            <Button class="px-lg py-sm font-label-md text-label-md bg-primary text-white rounded-lg shadow-sm hover:opacity-90 active:scale-95 transition-all">
              Analyze Now
            </Button>
          </NuxtLink>
        </div>
      </div>
    </nav>
    
    <!-- Hero Section -->
    <header class="relative pt-32 pb-2xl overflow-hidden">
      <div class="max-w-[1100px] mx-auto px-lg relative z-10">
        <div class="flex flex-col lg:flex-row items-center gap-3xl">
          <!-- Hero Content -->
          <div class="flex-1 text-center lg:text-left">
            <div class="inline-flex items-center gap-2 px-md py-xs bg-primary-fixed text-primary font-label-md text-label-md rounded-full mb-lg animate-fade-in">
              <span class="material-symbols-outlined text-[18px]">auto_awesome</span>
              <span>Powered by AI</span>
            </div>
            <h1 class="font-display text-display text-on-surface mb-md max-w-2xl mx-auto lg:mx-0">
              Know Exactly How Your Resume Stacks Up
            </h1>
            <p class="font-body-lg text-body-lg text-on-surface-variant mb-xl max-w-xl mx-auto lg:mx-0">
              Upload your resume, paste a job description, and get an AI analysis with match score, strengths, gaps, and actionable suggestions in seconds.
            </p>
            <div class="flex flex-col sm:flex-row items-center gap-md justify-center lg:justify-start mb-lg">
              <NuxtLink to="/register" class="w-full sm:w-auto">
                <Button class="w-full px-2xl py-md h-auto font-label-md text-body-md bg-primary text-white rounded-xl shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all flex items-center justify-center gap-2">
                  Analyze My Resume
                  <span class="material-symbols-outlined">arrow_forward</span>
                </Button>
              </NuxtLink>
              <Button variant="outline" class="w-full sm:w-auto px-2xl py-md h-auto font-label-md text-body-md border border-outline-variant text-on-surface-variant rounded-xl hover:bg-surface-container-low transition-all">
                See Sample Report
              </Button>
            </div>
            <div class="flex items-center justify-center lg:justify-start gap-4 text-on-surface-variant font-body-sm text-body-sm opacity-70">
              <div class="flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">credit_card_off</span>
                <span>No credit card required</span>
              </div>
              <span class="hidden sm:inline">•</span>
              <div class="flex items-center gap-1">
                <span class="material-symbols-outlined text-[16px]">timer</span>
                <span>Takes less than 30 seconds</span>
              </div>
            </div>
          </div>
          <!-- Hero Mockup -->
          <div class="flex-1 relative w-full max-w-[500px] lg:max-w-none">
            <div class="relative bg-white/80 backdrop-blur-md rounded-2xl p-lg shadow-2xl border border-outline-variant/30 overflow-hidden">
              <div class="flex justify-between items-start mb-xl">
                <div>
                  <h3 class="font-headline-sm text-headline-sm text-on-surface">Analysis Overview</h3>
                  <p class="font-body-sm text-body-sm text-on-surface-variant">Senior Product Designer @ Meta</p>
                </div>
                <span class="px-sm py-xs bg-emerald-100 text-emerald-700 text-label-sm font-label-sm rounded-lg">Live Analysis</span>
              </div>
              <div class="flex flex-col md:flex-row items-center gap-xl mb-xl">
                <!-- Circular Score -->
                <div class="relative w-40 h-40">
                  <svg class="w-full h-full" viewBox="0 0 100 100">
                    <circle class="text-surface-container stroke-current" cx="50" cy="50" fill="transparent" r="40" stroke-width="10"></circle>
                    <circle 
                      class="text-emerald-500 stroke-current transition-all duration-1000 ease-out" 
                      cx="50" cy="50" fill="transparent" r="40" stroke-linecap="round" stroke-width="10" 
                      style="transform: rotate(-90deg); transform-origin: 50% 50%; stroke-dasharray: 251.2;"
                      :style="`stroke-dashoffset: ${progressOffset};`"
                    ></circle>
                  </svg>
                  <div class="absolute inset-0 flex flex-col items-center justify-center">
                    <span class="font-display text-[32px] text-on-surface">{{ currentScore }}%</span>
                    <span class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider">Match</span>
                  </div>
                </div>
                <!-- Stats Column -->
                <div class="flex-1 space-y-md w-full">
                  <div class="p-md bg-emerald-50 rounded-xl flex items-center justify-between border border-emerald-100">
                    <div class="flex items-center gap-sm">
                      <span class="material-symbols-outlined text-emerald-600">check_circle</span>
                      <span class="font-label-md text-label-md text-emerald-900">4 Key Strengths</span>
                    </div>
                    <span class="material-symbols-outlined text-emerald-600">chevron_right</span>
                  </div>
                  <div class="p-md bg-amber-50 rounded-xl flex items-center justify-between border border-amber-100">
                    <div class="flex items-center gap-sm">
                      <span class="material-symbols-outlined text-amber-600">lightbulb</span>
                      <span class="font-label-md text-label-md text-amber-900">3 Suggestions</span>
                    </div>
                    <span class="material-symbols-outlined text-amber-600">chevron_right</span>
                  </div>
                </div>
              </div>
              <!-- Mini Resume Preview -->
              <div class="space-y-sm opacity-50 select-none">
                <div class="h-2 w-3/4 bg-on-surface-variant/20 rounded-full"></div>
                <div class="h-2 w-full bg-on-surface-variant/10 rounded-full"></div>
                <div class="h-2 w-5/6 bg-on-surface-variant/10 rounded-full"></div>
              </div>
            </div>
            <!-- Decorative Element -->
            <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-primary/10 rounded-full blur-3xl -z-10"></div>
            <div class="absolute -top-12 -left-12 w-48 h-48 bg-tertiary-fixed/20 rounded-full blur-3xl -z-10"></div>
          </div>
        </div>
      </div>
    </header>

    <!-- Features Bento Grid -->
    <section class="py-3xl max-w-[1100px] mx-auto px-lg">
      <div class="text-center mb-2xl">
        <h2 class="font-headline-lg text-headline-lg text-on-surface mb-sm">Everything you need to land the interview</h2>
        <p class="font-body-md text-body-md text-on-surface-variant max-w-2xl mx-auto">Our AI dissects every word of your resume to ensure you meet the specific criteria hiring managers are looking for.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-lg">
        <!-- Feature 1 -->
        <Card class="p-xl border-outline-variant/30 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-0 border-solid border-transparent ring-1 ring-outline-variant/30">
          <div class="w-12 h-12 bg-primary-fixed rounded-xl flex items-center justify-center mb-lg">
            <span class="material-symbols-outlined text-primary text-3xl">analytics</span>
          </div>
          <h3 class="font-headline-sm text-headline-sm mb-sm text-on-surface">Instant Match Score</h3>
          <p class="font-body-md text-body-md text-on-surface-variant">Get a definitive percentage score showing how well your experience aligns with specific job descriptions.</p>
        </Card>
        <!-- Feature 2 -->
        <Card class="p-xl border-outline-variant/30 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-0 border-solid border-transparent ring-1 ring-outline-variant/30">
          <div class="w-12 h-12 bg-secondary-fixed rounded-xl flex items-center justify-center mb-lg">
            <span class="material-symbols-outlined text-secondary text-3xl">troubleshoot</span>
          </div>
          <h3 class="font-headline-sm text-headline-sm mb-sm text-on-surface">Gap Analysis</h3>
          <p class="font-body-md text-body-md text-on-surface-variant">Identify missing keywords and technical requirements that are preventing you from passing ATS filters.</p>
        </Card>
        <!-- Feature 3 -->
        <Card class="p-xl border-outline-variant/30 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-0 border-solid border-transparent ring-1 ring-outline-variant/30">
          <div class="w-12 h-12 bg-tertiary-fixed rounded-xl flex items-center justify-center mb-lg">
            <span class="material-symbols-outlined text-tertiary text-3xl">auto_fix_high</span>
          </div>
          <h3 class="font-headline-sm text-headline-sm mb-sm text-on-surface">Actionable Suggestions</h3>
          <p class="font-body-md text-body-md text-on-surface-variant">Receive line-by-line advice on how to rephrase your bullet points for maximum impact and clarity.</p>
        </Card>
      </div>
    </section>

    <!-- Content Divider -->
    <div class="max-w-[1100px] mx-auto px-lg">
      <div class="h-px bg-outline-variant/20 w-full"></div>
    </div>

    <!-- Stats / Trust Section -->
    <section class="py-2xl max-w-[1100px] mx-auto px-lg text-center">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-xl">
        <div>
          <p class="font-display text-[32px] text-primary">50k+</p>
          <p class="font-label-md text-label-md text-on-surface-variant">Resumes Scanned</p>
        </div>
        <div>
          <p class="font-display text-[32px] text-primary">85%</p>
          <p class="font-label-md text-label-md text-on-surface-variant">Interview Rate</p>
        </div>
        <div>
          <p class="font-display text-[32px] text-primary">120+</p>
          <p class="font-label-md text-label-md text-on-surface-variant">Job Sites Covered</p>
        </div>
        <div>
          <p class="font-display text-[32px] text-primary">4.9/5</p>
          <p class="font-label-md text-label-md text-on-surface-variant">User Rating</p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-surface-container-lowest border-t border-outline-variant/20 py-xl mt-3xl">
      <div class="flex flex-col md:flex-row justify-between items-center px-lg max-w-[1100px] mx-auto gap-md">
        <div class="flex flex-col items-center md:items-start gap-sm">
          <span class="font-headline-sm text-headline-sm font-bold text-primary">ResumeAI</span>
          <p class="font-body-sm text-body-sm text-on-surface-variant">© 2024 ResumeAI. Analytical Clarity for Job Seekers.</p>
        </div>
        <div class="flex gap-lg">
          <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Privacy Policy</a>
          <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Terms of Service</a>
          <a class="font-body-sm text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Contact Support</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { Button } from '~/components/ui/button/index'
import { Card } from '~/components/ui/card/index'
import { useAuthStore } from '~/stores/auth'
import { useRouter } from 'vue-router'

definePageMeta({
  layout: false
})

const authStore = useAuthStore()
const router = useRouter()

// On mount, check if authenticated and maybe redirect, or just let them see the landing page
// If they are logged in and hit landing page, maybe they want to go to dashboard.
// We keep them on landing page, but the "Sign In" button could change to "Dashboard".

const scrolled = ref(false)
const progressOffset = ref(251.2) // circumference
const currentScore = ref(0)

let scrollHandler: () => void
let animationTimer: any

onMounted(() => {
  // Navigation shadow on scroll
  scrollHandler = () => {
    scrolled.value = window.scrollY > 20
  }
  window.addEventListener('scroll', scrollHandler)

  // Animate the progress ring (Target: 78%)
  animationTimer = setTimeout(() => {
    const targetScore = 78
    const circumference = 251.2
    
    // Animate the stroke offset
    progressOffset.value = circumference - (targetScore / 100 * circumference)
    
    // Counter animation
    let startTimestamp: number | null = null
    const duration = 1000 // 1 second
    
    const step = (timestamp: number) => {
      if (!startTimestamp) startTimestamp = timestamp
      const progress = Math.min((timestamp - startTimestamp) / duration, 1)
      
      // easeOutQuart
      const easeOut = 1 - Math.pow(1 - progress, 4)
      currentScore.value = Math.floor(easeOut * targetScore)
      
      if (progress < 1) {
        window.requestAnimationFrame(step)
      } else {
        currentScore.value = targetScore
      }
    }
    
    window.requestAnimationFrame(step)
  }, 500)
})

onUnmounted(() => {
  if (scrollHandler) {
    window.removeEventListener('scroll', scrollHandler)
  }
  if (animationTimer) {
    clearTimeout(animationTimer)
  }
})
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  vertical-align: middle;
}
</style>
