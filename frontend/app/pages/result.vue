<template>
  <div class="px-4 md:px-8 max-w-container_max mx-auto min-h-screen pt-8 pb-32">
    <div v-if="isLoading" class="flex justify-center items-center h-[60vh]">
      <span class="material-symbols-outlined animate-spin text-primary text-4xl">sync</span>
    </div>
    <div v-else-if="analysis">
      <!-- Header Actions -->
      <div class="flex flex-wrap items-center justify-between gap-4 mb-8 animate-fade-in" data-html2canvas-ignore="true">
        <div class="flex items-center gap-1">
          <NuxtLink to="/dashboard" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md">
            My Analyses
          </NuxtLink>
          <span class="material-symbols-outlined text-outline-variant text-[18px]">chevron_right</span>
          <span class="text-primary font-bold font-label-md text-label-md">{{ analysis.label || 'Untitled Analysis' }}</span>
        </div>
        
        <div class="flex items-center gap-3">
          <!-- Cover Letter Button -->
          <Button @click="handleGenerateCoverLetter" :disabled="isGenerating" class="bg-surface-container border border-outline-variant/40 !text-on-surface font-label-md text-label-md px-6 py-2 rounded-lg flex items-center gap-2 shadow-sm hover:-translate-y-0.5 transition-all hover:!text-white">
            <span class="material-symbols-outlined text-[18px]" v-if="!isGenerating">edit_note</span>
            <span class="material-symbols-outlined text-[18px] animate-spin" v-else>sync</span>
            {{ isGenerating ? 'Generating...' : 'Cover Letter' }}
          </Button>
          <!-- Download PDF Button -->
          <Button @click="exportToPDF" :disabled="isExporting" class="bg-primary !text-white font-label-md text-label-md px-6 py-2 rounded-lg flex items-center gap-2 shadow-md hover:-translate-y-0.5 transition-all">
            <span class="material-symbols-outlined text-[18px]" v-if="!isExporting">download</span>
            <span class="material-symbols-outlined text-[18px] animate-spin" v-else>sync</span>
            {{ isExporting ? 'Generating PDF...' : 'Download PDF' }}
          </Button>
        </div>
      </div>
      
      <!-- Report Container -->
      <div class="bg-[#f8fafc] p-2 rounded-xl">
      
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
                    :class="analysis.match_score >= 80 ? 'text-emerald-500' : analysis.match_score >= 60 ? 'text-amber-500' : 'text-error'"
                    class="transition-all duration-1000 ease-out" 
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
                  <span class="text-4xl font-bold text-on-surface leading-none">{{ Math.round(analysis.match_score) }}%</span>
                </div>
              </div>
              <div class="flex-1 text-center md:text-left">
                <div class="inline-flex items-center px-4 py-1 rounded-full font-label-md text-label-md mb-2"
                     :class="analysis.match_score >= 80 ? 'bg-emerald-100 text-emerald-700' : analysis.match_score >= 60 ? 'bg-amber-100 text-amber-700' : 'bg-error-container text-error'">
                  <span class="material-symbols-outlined text-[16px] mr-1" style="font-variation-settings: 'FILL' 1;">
                    {{ analysis.match_score >= 80 ? 'verified' : analysis.match_score >= 60 ? 'info' : 'warning' }}
                  </span>
                  {{ analysis.match_score >= 80 ? 'Good Match' : analysis.match_score >= 60 ? 'Average Match' : 'Needs Work' }}
                </div>
                <h2 class="text-2xl font-bold text-on-surface mb-1">Job Alignment Analysis</h2>
                <p class="text-on-surface-variant text-sm">Review the missing keywords and suggestions to improve your resume score.</p>
              </div>
            </div>
            
            <div class="grid grid-cols-2 gap-4 mt-8 pt-8 border-t border-outline-variant/20">
              <div class="text-center border-r border-outline-variant/20">
                <p class="text-rose-600 text-lg font-bold">{{ analysis.missing_keywords?.length || 0 }}</p>
                <p class="text-on-surface-variant text-xs font-bold uppercase tracking-wider">Missing Keywords</p>
              </div>
              <div class="text-center">
                <p class="text-primary text-lg font-bold">{{ analysis.suggestions?.length || 0 }}</p>
                <p class="text-on-surface-variant text-xs font-bold uppercase tracking-wider">Suggestions</p>
              </div>
            </div>
          </Card>
          
          <!-- Keywords Card -->
          <Card class="bg-white border-outline-variant/30 rounded-xl p-6 shadow-[0_1px_3px_rgba(0,0,0,0.08)] animate-fade-in border-0 ring-1 ring-outline-variant/30" style="animation-delay: 0.2s;">
            <div>
              <h3 class="text-lg font-bold text-on-surface mb-4">Keyword Gap Analysis</h3>
              <div class="flex flex-col gap-8">
                
                <div v-if="analysis.missing_keywords?.length">
                  <p class="text-sm font-bold text-on-surface-variant mb-2 flex items-center">
                    <span class="text-rose-500 mr-2 font-bold">Missing</span> ({{ analysis.missing_keywords.length }})
                  </p>
                  <div class="flex flex-wrap gap-2">
                    <span v-for="kw in analysis.missing_keywords" :key="kw" class="px-3 py-1 bg-rose-50 text-rose-700 border border-rose-200 rounded-lg text-xs font-medium">{{ kw }}</span>
                  </div>
                </div>
                <div v-else>
                  <p class="text-sm text-on-surface-variant">No missing keywords found! Great job.</p>
                </div>
                
              </div>
            </div>
          </Card>
          
          <!-- Bottom CTA -->
          <div class="flex justify-center mt-4" data-html2canvas-ignore="true">
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
            <div class="flex border-b border-outline-variant/20 bg-surface-container-low px-4 pt-4 overflow-x-auto" data-html2canvas-ignore="true">
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
            <div class="p-6 min-h-[400px] flex flex-col gap-8">
              
              <!-- Summary Tab -->
              <div v-show="activeTab === 'summary'">
                <h4 class="text-lg font-bold text-on-surface mb-4">Executive Summary</h4>
                <p class="text-on-surface-variant text-base leading-relaxed mb-4">
                  Based on the AI analysis, your resume has a {{ Math.round(analysis.match_score) }}% match score for this role.
                </p>
                <p class="text-on-surface-variant text-base leading-relaxed" v-if="analysis.missing_keywords?.length">
                  The primary gap lies in missing some key technical terms required by the job description, such as {{ analysis.missing_keywords.slice(0, 2).join(' and ') }}.
                </p>
                
                <div class="mt-8 p-4 bg-primary-fixed/10 border border-primary-fixed/30 rounded-lg" v-if="analysis.suggestions?.length">
                  <p class="text-primary font-bold text-sm flex items-center mb-1">
                    <span class="material-symbols-outlined text-[18px] mr-2">lightbulb</span>
                    AI Insight
                  </p>
                  <p class="text-on-surface-variant text-sm">
                    {{ analysis.suggestions[0] }}
                  </p>
                </div>
              </div>
              
              <!-- Suggestions Tab -->
              <div v-show="activeTab === 'suggestions'">
                <h4 class="text-lg font-bold text-on-surface mb-4">Recommended Changes</h4>
                <div class="space-y-4" v-if="analysis.suggestions?.length">
                  <div class="flex gap-4" v-for="(suggestion, idx) in analysis.suggestions" :key="idx">
                    <div class="w-8 h-8 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center flex-shrink-0 font-bold text-xs">{{ idx + 1 }}</div>
                    <p class="text-on-surface-variant text-base">{{ suggestion }}</p>
                  </div>
                </div>
                <p v-else class="text-sm text-on-surface-variant">No suggestions available.</p>
              </div>

              <!-- Hide other tabs if data is empty -->
              <div v-show="activeTab === 'strengths' || activeTab === 'weaknesses'" class="text-center py-12">
                <p class="text-sm text-on-surface-variant">This detail is not available in the current AI model output.</p>
              </div>
              
            </div>
          </Card>
        </div>
        
      </div>
      </div> <!-- End Report Container -->
    </div>
  </div>

  <!-- ── Cover Letter Modal ── -->
  <Teleport to="body">
    <div
      v-if="showCoverLetterModal"
      class="fixed inset-0 z-[9999] flex items-center justify-center p-4"
      @click.self="showCoverLetterModal = false"
    >
      <!-- Backdrop -->
      <div class="absolute inset-0 bg-black/60 backdrop-blur-sm" @click="showCoverLetterModal = false"></div>

      <!-- Modal Card -->
      <div class="relative z-10 w-full max-w-2xl max-h-[90vh] flex flex-col bg-surface rounded-2xl shadow-2xl border border-outline-variant/30 overflow-hidden">
        
        <!-- Modal Header -->
        <div class="flex items-center justify-between px-6 py-4 border-b border-outline-variant/20 bg-surface-container-low shrink-0">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-lg bg-primary-container flex items-center justify-center">
              <span class="material-symbols-outlined text-on-primary-container text-[20px]">edit_note</span>
            </div>
            <div>
              <h3 class="font-bold text-on-surface text-base">AI Cover Letter</h3>
              <p class="text-xs text-on-surface-variant">{{ analysis.label || 'Untitled Position' }}</p>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <Button
              @click="copyCoverLetter"
              variant="ghost"
              class="flex items-center gap-1 text-sm text-on-surface-variant hover:text-primary px-3 py-1.5 h-auto rounded-lg"
            >
              <span class="material-symbols-outlined text-[16px]">{{ copied ? 'check_circle' : 'content_copy' }}</span>
              {{ copied ? 'Copied!' : 'Copy' }}
            </Button>
            <Button
              @click="downloadCoverLetter"
              variant="ghost"
              class="flex items-center gap-1 text-sm text-on-surface-variant hover:text-primary px-3 py-1.5 h-auto rounded-lg"
            >
              <span class="material-symbols-outlined text-[16px]">download</span>
              Download
            </Button>
            <button @click="showCoverLetterModal = false" class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container transition-colors">
              <span class="material-symbols-outlined text-on-surface-variant text-[20px]">close</span>
            </button>
          </div>
        </div>

        <!-- Cover Letter Content -->
        <div class="flex-1 overflow-y-auto p-6">
          <div
            v-if="clError"
            class="flex items-start gap-3 p-4 bg-error-container rounded-xl mb-4"
          >
            <span class="material-symbols-outlined text-error text-[20px] shrink-0">error</span>
            <p class="text-on-error-container text-sm">{{ clError }}</p>
          </div>

          <textarea
            v-model="coverLetter"
            class="w-full min-h-[400px] bg-surface-container-low border border-outline-variant/30 rounded-xl p-5 text-on-surface text-sm leading-relaxed resize-y focus:outline-none focus:ring-2 focus:ring-primary/40 font-mono"
            placeholder="Your AI-generated cover letter will appear here..."
            spellcheck="true"
          />
        </div>

        <!-- Modal Footer -->
        <div class="px-6 py-4 border-t border-outline-variant/20 bg-surface-container-low shrink-0 flex items-center justify-between">
          <p class="text-xs text-on-surface-variant">✏️ You can edit the letter directly before copying or downloading.</p>
          <Button @click="showCoverLetterModal = false" variant="ghost" class="text-sm px-4 py-2 h-auto rounded-lg">Close</Button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Card } from '~/components/ui/card/index'
import { Button } from '~/components/ui/button/index'
import { useAnalysis } from '~/composables/useAnalysis'
import { useCoverLetter } from '~/composables/useCoverLetter'

definePageMeta({
  middleware: 'auth'
})

const route = useRoute()
const router = useRouter()
const { fetchAnalysis } = useAnalysis()

const tabs = [
  { id: 'summary', label: 'Summary' },
  { id: 'strengths', label: 'Strengths' },
  { id: 'weaknesses', label: 'Weaknesses' },
  { id: 'suggestions', label: 'Suggestions' }
]

const activeTab = ref('summary')
const analysis = ref<any>(null)
const isLoading = ref(true)
const isExporting = ref(false)

// Cover Letter state
const { coverLetter, isGenerating, error: clError, generateCoverLetter } = useCoverLetter()
const showCoverLetterModal = ref(false)
const copied = ref(false)

// Progress ring animation
const dashOffset = ref(251.2) // Start empty (2 * PI * r = 251.2 for r=40)

// Cover Letter Handlers
const handleGenerateCoverLetter = async () => {
  const id = route.query.id as string
  if (!id) return
  showCoverLetterModal.value = true
  await generateCoverLetter(id)
}

const copyCoverLetter = async () => {
  if (!coverLetter.value) return
  await navigator.clipboard.writeText(coverLetter.value)
  copied.value = true
  setTimeout(() => { copied.value = false }, 2000)
}

const downloadCoverLetter = () => {
  if (!coverLetter.value) return
  const blob = new Blob([coverLetter.value], { type: 'text/plain' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `CoverLetter_${analysis.value?.label || 'ResumeAI'}.txt`
  a.click()
  URL.revokeObjectURL(url)
}

const exportToPDF = async () => {
  if (!analysis.value) return
  isExporting.value = true
  
  try {
    const { jsPDF } = await import('jspdf')
    const doc = new jsPDF({ unit: 'mm', format: 'a4', orientation: 'portrait' })
    
    const pageW = doc.internal.pageSize.getWidth()
    const pageH = doc.internal.pageSize.getHeight()
    const marginX = 20
    const contentW = pageW - marginX * 2
    let y = 20
    
    const checkNewPage = (neededHeight: number) => {
      if (y + neededHeight > pageH - 20) {
        doc.addPage()
        y = 20
      }
    }
    
    const addText = (text: string, options: { fontSize?: number, bold?: boolean, color?: [number, number, number], maxWidth?: number } = {}) => {
      const { fontSize = 11, bold = false, color = [30, 30, 30], maxWidth = contentW } = options
      doc.setFontSize(fontSize)
      doc.setFont('helvetica', bold ? 'bold' : 'normal')
      doc.setTextColor(color[0], color[1], color[2])
      const lines = doc.splitTextToSize(text, maxWidth)
      const lineHeight = fontSize * 0.45
      checkNewPage(lines.length * lineHeight + 4)
      doc.text(lines, marginX, y)
      y += lines.length * lineHeight + 4
    }
    
    const addDivider = (color: [number, number, number] = [200, 200, 200]) => {
      checkNewPage(6)
      doc.setDrawColor(color[0], color[1], color[2])
      doc.setLineWidth(0.4)
      doc.line(marginX, y, pageW - marginX, y)
      y += 6
    }
    
    // ─── HEADER ───
    doc.setFillColor(30, 30, 50)
    doc.rect(0, 0, pageW, 38, 'F')
    doc.setFontSize(22)
    doc.setFont('helvetica', 'bold')
    doc.setTextColor(255, 255, 255)
    doc.text('Resume Analysis Report', marginX, 16)
    doc.setFontSize(10)
    doc.setFont('helvetica', 'normal')
    doc.setTextColor(180, 180, 210)
    const dateStr = analysis.value.created_at
      ? new Date(analysis.value.created_at).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
      : new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    doc.text(`Target Role: ${analysis.value.label || 'Untitled Position'}   |   Generated: ${dateStr}`, marginX, 26)
    
    // Match score badge
    const score = Math.round(analysis.value.match_score)
    const scoreColor: [number, number, number] = score >= 80 ? [16, 185, 129] : score >= 60 ? [245, 158, 11] : [239, 68, 68]
    doc.setFillColor(...scoreColor)
    doc.roundedRect(pageW - marginX - 28, 6, 28, 26, 3, 3, 'F')
    doc.setFontSize(20)
    doc.setFont('helvetica', 'bold')
    doc.setTextColor(255, 255, 255)
    doc.text(`${score}%`, pageW - marginX - 14, 22, { align: 'center' })
    
    y = 50
    
    // ─── EXECUTIVE SUMMARY ───
    addText('Executive Summary', { fontSize: 15, bold: true })
    addDivider()
    const summaryVerdict = score >= 80
      ? 'This indicates a strong alignment with the role\'s requirements.'
      : score >= 60
        ? 'This indicates an average alignment. Addressing the keyword gaps below will significantly improve your chances.'
        : 'This indicates significant gaps between your resume and the role\'s requirements. A major revision is recommended.'
    addText(
      `This report provides an AI-driven analysis of your resume against the provided job description. Your current resume achieves a ${score}% match score. ${summaryVerdict}`,
      { fontSize: 11, color: [80, 80, 80] }
    )
    y += 6
    
    // ─── MISSING KEYWORDS ───
    const keywords = analysis.value.missing_keywords || []
    addText('Missing Keywords', { fontSize: 15, bold: true })
    addDivider()
    if (keywords.length > 0) {
      addText(`The following ${keywords.length} critical keywords from the job description are missing from your resume:`, { fontSize: 10, color: [100, 100, 100] })
      y += 2
      // Two-column layout for keywords
      const col1 = keywords.filter((_: string, i: number) => i % 2 === 0)
      const col2 = keywords.filter((_: string, i: number) => i % 2 === 1)
      const rows = Math.max(col1.length, col2.length)
      const rowH = 7
      for (let i = 0; i < rows; i++) {
        checkNewPage(rowH)
        doc.setFontSize(10)
        doc.setFont('helvetica', 'normal')
        doc.setTextColor(60, 60, 60)
        if (col1[i]) {
          doc.text(`• ${col1[i]}`, marginX + 2, y)
        }
        if (col2[i]) {
          doc.text(`• ${col2[i]}`, marginX + contentW / 2, y)
        }
        y += rowH
      }
    } else {
      addText('No missing keywords found. Your resume covers all key terms!', { fontSize: 11, color: [16, 185, 129] })
    }
    y += 6
    
    // ─── SUGGESTIONS ───
    const suggestions = analysis.value.suggestions || []
    addText('Recommended Improvements', { fontSize: 15, bold: true })
    addDivider()
    if (suggestions.length > 0) {
      for (let i = 0; i < suggestions.length; i++) {
        const suggestion = suggestions[i]
        const lines = doc.splitTextToSize(suggestion, contentW - 12)
        const blockH = lines.length * 5 + 8
        checkNewPage(blockH)
        // Number badge
        doc.setFillColor(238, 242, 255)
        doc.roundedRect(marginX, y - 4, 8, 7, 1, 1, 'F')
        doc.setFontSize(9)
        doc.setFont('helvetica', 'bold')
        doc.setTextColor(99, 102, 241)
        doc.text(`${i + 1}`, marginX + 4, y + 1, { align: 'center' })
        // Text
        doc.setFontSize(10.5)
        doc.setFont('helvetica', 'normal')
        doc.setTextColor(50, 50, 50)
        doc.text(lines, marginX + 12, y + 1)
        y += lines.length * 5 + 8
      }
    } else {
      addText('No further suggestions available.', { fontSize: 11, color: [150, 150, 150] })
    }
    
    // ─── FOOTER ───
    const totalPages = (doc.internal as any).getNumberOfPages()
    for (let p = 1; p <= totalPages; p++) {
      doc.setPage(p)
      doc.setFillColor(245, 245, 250)
      doc.rect(0, pageH - 12, pageW, 12, 'F')
      doc.setFontSize(8)
      doc.setFont('helvetica', 'normal')
      doc.setTextColor(160, 160, 180)
      doc.text('Generated automatically by ResumeAI', marginX, pageH - 5)
      doc.text(`Page ${p} of ${totalPages}`, pageW - marginX, pageH - 5, { align: 'right' })
    }
    
    doc.save(`ResumeAI_Report_${analysis.value.label || 'Doc'}.pdf`)
  } catch (error) {
    console.error('Failed to export PDF', error)
    alert('Failed to generate PDF. Please try again.')
  } finally {
    isExporting.value = false
  }
}

onMounted(async () => {
  const id = route.query.id as string
  if (!id) {
    router.push('/dashboard')
    return
  }
  
  const result = await fetchAnalysis(id)
  if (result.success && result.data) {
    analysis.value = result.data
    // Animate to score
    setTimeout(() => {
      dashOffset.value = 251.2 - ((analysis.value.match_score / 100) * 251.2)
    }, 300)
  } else {
    alert('Failed to load analysis')
    router.push('/dashboard')
  }
  isLoading.value = false
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
