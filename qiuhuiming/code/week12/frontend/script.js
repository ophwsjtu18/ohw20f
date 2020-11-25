// get the buttons 
const upButton = document.querySelector('#up-button')
const downButton = document.querySelector('#down-button')
const leftButton = document.querySelector('#left-button')
const rightButton = document.querySelector('#right-button')
const arrowButtons = [upButton, downButton, leftButton, rightButton]

const clickCallbackFactory = (id) => {
    return () => {
        const arrow = id.substring(0, id.indexOf('-'))
        console.log(arrow)
        $.get('/cgi-bin/handle_arrow.py', 
        {
            arrow
        })
    }
}

arrowButtons.forEach((button) => {
    button.addEventListener('click', clickCallbackFactory(button.id))
}
)