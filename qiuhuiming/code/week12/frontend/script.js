const upButton = document.querySelector('#up-button')
const downButton = document.querySelector('#down-button')
const leftButton = document.querySelector('#left-button')
const rightButton = document.querySelector('#right-button')
const cycleButton = document.querySelector('#cycle-button')
const arrowButtons = [upButton, downButton, leftButton, rightButton, cycleButton]

const sendMoveArrowFunction = (arrow) => {
    const action = '/cgi-bin/handle_arrow.py'
    return () => {
        $.get(action, { arrow })
        console.log(`sendMoveInstruction: ${arrow}`)
    }
}

arrowButtons.forEach((button) => {
    const arrow = button.id.substring(0, button.id.indexOf('-'))
    button.addEventListener('click', sendMoveArrowFunction(arrow))
}
)