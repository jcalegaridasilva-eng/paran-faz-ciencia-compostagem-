// Remove Loading Screen
window.addEventListener("load", () => {
    const loader = document.querySelector(".loader-wrapper");
    loader.style.opacity = "0";
    setTimeout(() => {
        loader.style.display = "none";
    }, 500);

    // GSAP Animations (Hero Section)
    gsap.from(".gsap-title", { duration: 1, y: -50, opacity: 0, ease: "power3.out", delay: 0.5 });
    gsap.from(".gsap-subtitle", { duration: 1, y: 30, opacity: 0, ease: "power3.out", delay: 0.8 });
    gsap.from(".gsap-btn", { duration: 1, scale: 0.5, opacity: 0, ease: "back.out(1.7)", delay: 1.1 });
});

// Inicialização do AOS (Scroll Reveal)
AOS.init({
    duration: 1000,
    once: true, // Anima apenas na primeira vez que descer a tela
    offset: 100
});

// Efeito no Menu Fixo ao scrollar
window.addEventListener("scroll", () => {
    const nav = document.getElementById("navbar");
    if (window.scrollY > 50) {
        nav.style.padding = "10px 50px";
        nav.style.background = "rgba(255, 255, 255, 1)";
    } else {
        nav.style.padding = "15px 50px";
        nav.style.background = "rgba(255, 255, 255, 0.95)";
    }
});