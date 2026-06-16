<template>
  <main class="flex min-h-screen bg-background font-sans text-foreground overflow-hidden m-0 p-0">
    <!-- Left Section: Authentication Form -->
    <section class="w-full lg:w-1/2 bg-background flex flex-col items-center justify-center px-6 py-16 relative z-10">
      <div class="max-w-md w-full">
        <slot />
      </div>
    </section>

    <!-- Right Section: Visual & Testimonial -->
    <section class="hidden lg:flex w-1/2 bg-gradient-to-br from-primary via-[#6750a4] to-[#e1d4fd] relative items-center justify-center overflow-hidden">
      <!-- Decorative Grid -->
      <div class="absolute inset-0 bg-[radial-gradient(rgba(255,255,255,0.1)_1px,transparent_1px)] [background-size:32px_32px] opacity-30"></div>
      
      <!-- Atmospheric Element -->
      <div class="absolute top-0 left-0 w-full h-full pointer-events-none">
        <div class="absolute w-[500px] h-[500px] bg-[#e9ddff]/20 rounded-full blur-[120px] -top-48 -left-48"></div>
        <div class="absolute w-[400px] h-[400px] bg-[#e9ddff]/20 rounded-full blur-[100px] -bottom-32 -right-32"></div>
      </div>
      
      <!-- Floating Testimonial Card -->
      <div class="animate-[float_6s_ease-in-out_infinite] z-20 max-w-sm relative">
        <div class="bg-white/10 backdrop-blur-xl border border-white/20 p-8 rounded-2xl shadow-2xl">
          <div class="flex items-center gap-4 mb-6">
            <img alt="User Avatar" class="w-12 h-12 rounded-full border-2 border-[#e9ddff] object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDvikFbGe5w1MW0Bnx3TMTJEJGAIXDvBVaLl7pgsMTmR3BlCbafk3WjtM3PIaRvLhqvChrH70w6lkz2upMB06ZicGzoHz1HXuZkBhJCn6jA5kvemuUN38VHKAvOSkguNRzokhXLPcFbLzGyOWZ0fCUFvLuH7UocCVgiotQEE5sXhl3dpxirC6R_JwbnQgHn3xNRzseCMkzzzIXjKVTdFkcRy39Esv09J9H2jL42B7MaX-8_H7q3CCG5nUlANNr4gJimgJSubRpBmZ0">
            <div>
              <h4 class="text-sm font-semibold text-white">Sarah Jenkins</h4>
              <p class="text-xs text-white/70">UX Designer</p>
            </div>
          </div>
          <p class="text-lg text-white italic mb-6 leading-relaxed">
            "Finally know why my resume wasn't getting callbacks."
          </p>
          <div class="flex gap-1">
            <svg class="w-5 h-5 text-[#ffdf93] fill-current" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg class="w-5 h-5 text-[#ffdf93] fill-current" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg class="w-5 h-5 text-[#ffdf93] fill-current" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg class="w-5 h-5 text-[#ffdf93] fill-current" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
            <svg class="w-5 h-5 text-white/30 fill-current" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          </div>
        </div>
        
        <!-- Secondary Floating Chip -->
        <div class="absolute -bottom-6 -right-6 bg-emerald-100/90 backdrop-blur-sm px-4 py-2 rounded-full shadow-lg border border-emerald-200 flex items-center gap-2">
          <svg class="w-5 h-5 text-emerald-700" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
          <span class="text-emerald-700 font-bold text-sm">ATS Score: 92%</span>
        </div>
      </div>
    </section>
  </main>
</template>

<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}
</style>
