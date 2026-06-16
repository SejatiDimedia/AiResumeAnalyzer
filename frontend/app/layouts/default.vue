<template>
  <div class="font-body-md text-on-surface bg-[#f8fafc] min-h-screen flex flex-col">
    <!-- Top Navigation Bar -->
    <header class="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-md border-b border-outline-variant/30 shadow-sm transition-all duration-300">
      <div class="flex justify-between items-center px-lg py-sm max-w-container_max mx-auto h-16">
        <div class="flex items-center gap-md">
          <NuxtLink to="/dashboard" class="font-headline-md text-headline-md font-bold text-primary">ResumeAI</NuxtLink>
        </div>
        
        <nav class="hidden md:flex items-center gap-xl">
          <NuxtLink to="/dashboard" class="font-body-md text-body-md text-primary font-bold border-b-2 border-primary pb-1">History</NuxtLink>
          <NuxtLink to="/analyze" class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors">Analysis</NuxtLink>
          <NuxtLink to="/profile" class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors">Profile</NuxtLink>
          <NuxtLink to="/settings" class="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors">Settings</NuxtLink>
        </nav>
        
        <div class="flex items-center gap-md">
          <button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-variant/50 p-2 rounded-full transition-all">notifications</button>
          
          <div class="relative group cursor-pointer" @click="handleLogout">
            <div class="w-10 h-10 rounded-full border-2 border-primary/20 overflow-hidden">
              <img alt="Avatar" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAJL7bZHAvrOF0UnQhZO-x-AHn6ifXILbGNwj_qcz8YT8b5GuPlL5-m0HLsc8PQtlTW1UM-SXeTK5SesQumWMf6V-RL12iQi7xuwanSZwat34gdmghP85weYMx8JK7VPeIGP0MM2eF4rVZtMDQEcC-NmrlT729HjY4Gts1OCpuuFbesJ-Cf93T9fXdxbiO-9NcOgya7XQxF-m-4cuCNh5pFp9AyiEvku8zACriDwsw2smhThW4l8qpAPxNA91PHoauBBM-0IXig8hw" />
            </div>
            <!-- Logout tooltip -->
            <div class="absolute right-0 mt-2 w-32 bg-white rounded-md shadow-lg py-1 z-50 hidden group-hover:block border border-outline-variant/20">
              <span class="block px-4 py-2 text-sm text-error hover:bg-error-container/20 font-semibold text-center">Logout</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col pt-24 pb-32 px-4 max-w-container_max mx-auto w-full">
      <slot />
    </div>

    <!-- Bottom Navigation (Mobile) -->
    <nav class="fixed bottom-0 left-0 w-full z-50 bg-surface border-t border-outline-variant shadow-lg md:hidden rounded-t-xl pb-safe">
      <div class="flex justify-around items-center px-4 py-3 h-20">
        <!-- Home (Active) -->
        <NuxtLink to="/dashboard" class="flex flex-col items-center justify-center text-primary font-bold bg-primary-fixed/20 rounded-xl px-4 py-1 scale-110 transition-transform duration-200" active-class="text-primary font-bold bg-primary-fixed/20 scale-110" inactive-class="text-on-surface-variant scale-100 bg-transparent font-normal">
          <span class="material-symbols-outlined mb-1">home</span>
          <span class="font-label-sm text-[11px]">Home</span>
        </NuxtLink>
        <!-- Analyze (Center Action) -->
        <NuxtLink to="/analyze" class="flex flex-col items-center justify-center text-on-surface-variant hover:bg-surface-variant active:scale-110 transition-transform duration-200 group">
          <div class="bg-primary p-3 rounded-full -mt-10 shadow-lg text-white group-hover:bg-primary/90 transition-colors">
            <span class="material-symbols-outlined text-[32px]">add</span>
          </div>
          <span class="font-label-sm text-[11px] mt-1 group-hover:text-primary transition-colors">Analyze</span>
        </NuxtLink>
        <!-- Profile -->
        <NuxtLink to="/profile" class="flex flex-col items-center justify-center text-on-surface-variant hover:bg-surface-variant transition-colors duration-200 px-4 py-1 rounded-xl" active-class="text-primary font-bold bg-primary-fixed/20" inactive-class="text-on-surface-variant bg-transparent font-normal">
          <span class="material-symbols-outlined mb-1">person</span>
          <span class="font-label-sm text-[11px]">Profile</span>
        </NuxtLink>
      </div>
    </nav>

    <!-- Footer -->
    <footer class="w-full py-xl border-t border-outline-variant/20 bg-surface-container-lowest mt-auto">
      <div class="flex flex-col md:flex-row justify-between items-center px-lg max-w-container_max mx-auto gap-md">
        <div class="flex flex-col gap-sm text-center md:text-left">
          <span class="font-headline-sm text-headline-sm font-bold text-primary">ResumeAI</span>
          <p class="text-body-sm text-on-surface-variant">© 2024 ResumeAI. Analytical Clarity for Job Seekers.</p>
        </div>
        <div class="flex gap-lg">
          <a class="text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Privacy Policy</a>
          <a class="text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Terms of Service</a>
          <a class="text-body-sm text-on-surface-variant hover:text-primary transition-colors" href="#">Contact Support</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth'
import { useAuth } from '~/composables/useAuth'

const authStore = useAuthStore()
const { logout } = useAuth()

function handleLogout() {
  logout()
}
</script>

<style scoped>
.pb-safe {
  padding-bottom: env(safe-area-inset-bottom);
}
</style>
