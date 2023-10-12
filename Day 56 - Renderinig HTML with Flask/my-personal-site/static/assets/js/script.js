const words = ["Python Developer", "Web Developer", "UI/UX Designer"];
let i = 0;
let j = 0;
let isErasing = false;
let typingSpeed = 50; // Adjust typing speed (in milliseconds)
let eraseSpeed = 20; // Adjust erasing speed (in milliseconds)
let waitTime = 1000; // Time to wait before erasing (in milliseconds)

function typeWriter() {
    const currentWord = words[i];
    if (isErasing) {
        if (j > 0) {
            document.getElementById("typewriter-text").textContent = currentWord.slice(0, j - 1);
            j--;
            setTimeout(typeWriter, eraseSpeed);
        } else {
            isErasing = false;
            i = (i + 1) % words.length;
            setTimeout(typeWriter, waitTime);
        }
    } else {
        if (j < currentWord.length) {
            document.getElementById("typewriter-text").textContent = currentWord.slice(0, j + 1);
            j++;
            setTimeout(typeWriter, typingSpeed);
        } else {
            isErasing = true;
            setTimeout(typeWriter, waitTime);
        }
    }
}
typeWriter();