let vinyls = Array.from(document.getElementsByClassName('vinyl'))
vinyls.forEach((vinyl, idx) => {
    setTimeout(() => {
        vinyl.classList.add('fade-in')
        console.log('hi')
    }, (idx + 1) * 100)
})

console.log(vinyls)

console.log('hi')