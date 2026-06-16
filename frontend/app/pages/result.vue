<template>
  <div class="px-4 md:px-8 max-w-container_max mx-auto min-h-screen pt-8 pb-32">
    <!-- Breadcrumbs -->
    <div class="flex items-center gap-1 mb-8 animate-fade-in">
      <NuxtLink to="/dashboard" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md">
        My Analyses
      </NuxtLink>
      <span class="material-symbols-outlined text-outline-variant text-[18px]">chevron_right</span>
      <span class="text-primary font-bold font-label-md text-label-md">Backend Engineer — Tokopedia</span>
    </div>
    
    <!-- 2-Column Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      
      <!-- Left Column (60%) -->
      <div class="lg:col-span-7 flex flex-col gap-6">
        
        <!-- Score Card -->
        <Card class="bg-white border-outline-variant/30 rounded-xl p-6 shadow-[0_1px_3px_rgba(0,0,0,0.08)] animate-fade-in border-0 ring-1 ring-outline-variant/30" style="animation-delay: 0.1s;">
          <div class="flex flex-col md:flex-row items-center gap-8">
            <div class="relative w-[120px] h-[120px] flex items-center justify-center shrink-0">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                <circle class="text-surface-container-high" cx="50" cy="50" fill="transparent" r="40" stroke="currentColor" stroke-width="8"></circle>
                <circle 
                  class="text-emerald-500 transition-all duration-1000 ease-out" 
                  cx="50" 
                  cy="50" 
                  fill="transparent" 
                  r="40" 
                  stroke="currentColor" 
                  stroke-dasharray="251.2" 
                  :stroke-dashoffset="dashOffset" 
                  stroke-linecap="round" 
                  stroke-width="8">
                </circle>
              </svg>
              <div class="absolute flex flex-col items-center">
                <span class="text-4xl font-bold text-on-surface leading-none">78%</span>
              </div>
            </div>
            <div class="flex-1 text-center md:text-left">
              <div class="inline-flex items-center px-4 py-1 bg-emerald-100 text-emerald-700 rounded-full font-label-md text-label-md mb-2">
                <span class="material-symbols-outlined text-[16px] mr-1" style="font-variation-settings: 'FILL' 1;">verified</span>
                Good Match
              </div>
              <h2 class="text-2xl font-bold text-on-surface mb-1">Job Alignment Analysis</h2>
              <p class="text-on-surface-variant text-sm">Your resume shows strong proficiency in backend fundamentals but lacks specific infrastructure keywords required for this role.</p>
            </div>
          </div>
          
          <div class="grid grid-cols-3 gap-4 mt-8 pt-8 border-t border-outline-variant/20">
            <div class="text-center">
              <p class="text-emerald-600 text-lg font-bold">4</p>
              <p class="text-on-surface-variant text-xs font-bold uppercase tracking-wider">Strengths</p>
            </div>
            <div class="text-center border-x border-outline-variant/20">
              <p class="text-rose-600 text-lg font-bold">3</p>
              <p class="text-on-surface-variant text-xs font-bold uppercase tracking-wider">Weaknesses</p>
            </div>
            <div class="text-center">
              <p class="text-primary text-lg font-bold">5</p>
              <p class="text-on-surface-variant text-xs font-bold uppercase tracking-wider">Suggestions</p>
            </div>
          </div>
        </Card>
        
        <!-- Keywords Card -->
        <Card class="bg-white border-outline-variant/30 rounded-xl p-6 shadow-[0_1px_3px_rgba(0,0,0,0.08)] animate-fade-in border-0 ring-1 ring-outline-variant/30" style="animation-delay: 0.2s;">
          <div>
            <h3 class="text-lg font-bold text-on-surface mb-4">Keyword Gap Analysis</h3>
            <div class="flex flex-col gap-8">
              
              <div>
                <p class="text-sm font-bold text-on-surface-variant mb-2 flex items-center">
                  <span class="text-emerald-500 mr-2 font-bold">Matched</span> (4)
                </p>
                <div class="flex flex-wrap gap-2">
                  <span class="px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg text-xs font-medium">Python</span>
                  <span class="px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg text-xs font-medium">FastAPI</span>
                  <span class="px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg text-xs font-medium">PostgreSQL</span>
                  <span class="px-3 py-1 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-lg text-xs font-medium">Microservices</span>
                </div>
              </div>
              
              <div>
                <p class="text-sm font-bold text-on-surface-variant mb-2 flex items-center">
                  <span class="text-rose-500 mr-2 font-bold">Missing</span> (3)
                </p>
                <div class="flex flex-wrap gap-2">
                  <span class="px-3 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded-lg text-xs font-medium">Docker</span>
                  <span class="px-3 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded-lg text-xs font-medium">Kubernetes</span>
                  <span class="px-3 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded-lg text-xs font-medium">Redis</span>
                </div>
              </div>
              
            </div>
          </div>
        </Card>
        
        <!-- Bottom CTA -->
        <div class="flex justify-center mt-4">
          <NuxtLink to="/analyze">
            <Button variant="ghost" class="flex items-center gap-2 text-on-surface-variant hover:text-primary border border-transparent hover:border-primary/20 hover:bg-primary-fixed/30 px-8 py-6 rounded-lg transition-all font-bold text-sm group h-auto">
              <span class="material-symbols-outlined text-[20px] group-hover:rotate-180 transition-transform duration-500">refresh</span>
              Analyze Another Resume
            </Button>
          </NuxtLink>
        </div>
        
      </div>
      
      <!-- Right Column (40%) -->
      <div class="lg:col-span-5">
        <Card class="bg-white border-outline-variant/30 rounded-xl overflow-hidden shadow-[0_1px_3px_rgba(0,0,0,0.08)] sticky top-24 animate-fade-in border-0 ring-1 ring-outline-variant/30" style="animation-delay: 0.3s;">
          
          <!-- Tabs Header -->
          <div class="flex border-b border-outline-variant/20 bg-surface-container-low px-4 pt-4 overflow-x-auto">
            <button 
              v-for="tab in tabs" :key="tab.id"
              class="px-4 py-3 text-sm font-bold border-b-2 transition-all whitespace-nowrap"
              :class="activeTab === tab.id ? 'border-primary text-primary' : 'border-transparent text-on-surface-variant hover:text-primary'"
              @click="activeTab = tab.id"
            >
              {{ tab.label }}
            </button>
          </div>
          
          <!-- Tab Content -->
          <div class="p-6 min-h-[400px]">
            
            <!-- Summary Tab -->
            <div v-show="activeTab === 'summary'">
              <h4 class="text-lg font-bold text-on-surface mb-4">Executive Summary</h4>
              <p class="text-on-surface-variant text-base leading-relaxed mb-4">
                Your profile is highly competitive for the Backend Engineer position at Tokopedia. You demonstrate deep technical expertise in the core stack (Python/FastAPI). 
              </p>
              <p class="text-on-surface-variant text-base leading-relaxed">
                The primary gap lies in cloud-native deployment experience. Tokopedia relies heavily on container orchestration, which isn't explicitly detailed in your current resume version.
              </p>
              
              <div class="mt-8 p-4 bg-primary-fixed/10 border border-primary-fixed/30 rounded-lg">
                <p class="text-primary font-bold text-sm flex items-center mb-1">
                  <span class="material-symbols-outlined text-[18px] mr-2">lightbulb</span>
                  AI Insight
                </p>
                <p class="text-on-surface-variant text-sm">
                  Adding just one project related to Kubernetes could boost your match score by up to 12%.
                </p>
              </div>
            </div>
            
            <!-- Strengths Tab -->
            <div v-show="activeTab === 'strengths'">
              <h4 class="text-lg font-bold text-on-surface mb-4">Technical Strengths</h4>
              <ul class="space-y-4">
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-emerald-600 text-[16px] font-bold">check</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">Language Mastery</p>
                    <p class="text-on-surface-variant text-sm">Advanced Python 3.10+ usage demonstrated via asynchronous backend projects.</p>
                  </div>
                </li>
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-emerald-600 text-[16px] font-bold">check</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">API Architecture</p>
                    <p class="text-on-surface-variant text-sm">Strong understanding of RESTful principles and FastAPI implementation.</p>
                  </div>
                </li>
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-emerald-600 text-[16px] font-bold">check</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">Database Management</p>
                    <p class="text-on-surface-variant text-sm">Extensive experience with PostgreSQL and SQLAlchemy ORM optimization.</p>
                  </div>
                </li>
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-emerald-600 text-[16px] font-bold">check</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">System Performance</p>
                    <p class="text-on-surface-variant text-sm">Proven track record of improving latency by 40% in previous role.</p>
                  </div>
                </li>
              </ul>
            </div>
            
            <!-- Weaknesses Tab -->
            <div v-show="activeTab === 'weaknesses'">
              <h4 class="text-lg font-bold text-on-surface mb-4">Areas for Improvement</h4>
              <ul class="space-y-4">
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-rose-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-rose-600 text-[16px] font-bold">close</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">DevOps & Tooling</p>
                    <p class="text-on-surface-variant text-sm">Missing Docker and CI/CD pipeline experience mentioned in requirements.</p>
                  </div>
                </li>
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-rose-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-rose-600 text-[16px] font-bold">close</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">Caching Strategies</p>
                    <p class="text-on-surface-variant text-sm">No mention of Redis or Memcached for distributed caching.</p>
                  </div>
                </li>
                <li class="flex gap-4 items-start">
                  <div class="mt-1 w-6 h-6 rounded-full bg-rose-100 flex items-center justify-center flex-shrink-0">
                    <span class="material-symbols-outlined text-rose-600 text-[16px] font-bold">close</span>
                  </div>
                  <div>
                    <p class="font-bold text-sm text-on-surface">Scale Handling</p>
                    <p class="text-on-surface-variant text-sm">Lack of specific experience with large-scale message brokers like Kafka.</p>
                  </div>
                </li>
              </ul>
            </div>
            
            <!-- Suggestions Tab -->
            <div v-show="activeTab === 'suggestions'">
              <h4 class="text-lg font-bold text-on-surface mb-4">Recommended Changes</h4>
              <div class="space-y-4">
                <div class="flex gap-4">
                  <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">1</div>
                  <p class="text-on-surface-variant text-base">Integrate <span class="text-primary font-bold">Docker</span> into your 'Skills' section under Tools.</p>
                </div>
                <div class="flex gap-4">
                  <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">2</div>
                  <p class="text-on-surface-variant text-base">Rewrite the 'Stock Prediction' project to highlight <span class="text-primary font-bold">distributed systems</span>.</p>
                </div>
                <div class="flex gap-4">
                  <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">3</div>
                  <p class="text-on-surface-variant text-base">Mention your familiarity with <span class="text-primary font-bold">GCP or AWS</span> even if self-taught.</p>
                </div>
                <div class="flex gap-4">
                  <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">4</div>
                  <p class="text-on-surface-variant text-base">Add a <span class="text-primary font-bold">Testing</span> sub-section covering PyTest and TDD.</p>
                </div>
                <div class="flex gap-4">
                  <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">5</div>
                  <p class="text-on-surface-variant text-base">Quantify achievements using the <span class="text-primary font-bold">STAR method</span> for all roles.</p>
                </div>
              </div>
            </div>
            
          </div>
        </Card>
      </div>
      
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Card } from '~/components/ui/card/index'
import { Button } from '~/components/ui/button/index'

definePageMeta({
  // middleware: 'auth'
})

const tabs = [
  { id: 'summary', label: 'Summary' },
  { id: 'strengths', label: 'Strengths' },
  { id: 'weaknesses', label: 'Weaknesses' },
  { id: 'suggestions', label: 'Suggestions' }
]

const activeTab = ref('summary')

// Progress ring animation
const dashOffset = ref(251.2) // Start empty (2 * PI * r = 251.2 for r=40)

onMounted(() => {
  // Animate to 78% after a short delay
  setTimeout(() => {
    dashOffset.value = 251.2 - (0.78 * 251.2)
  }, 300)
})
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.5s ease-out forwards;
  opacity: 0;
}
</style>
