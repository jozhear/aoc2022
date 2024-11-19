document.addEventListener('DOMContentLoaded', async function (event) {

    var directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    // turn the html input into a workable Javascript variable
    var puzzle = document.querySelector(".jozPuzzle").textContent
    var puzzleArray = JSON.stringify(puzzle)
    var puzzleSplit = puzzleArray.split('\\n            ')
    puzzleSplit.shift()
    var puzzleGrid = []
    for (let row of puzzleSplit) {
        newListRow = []
        for (let letter of row) {
            newListRow.push(letter)
        }
        puzzleGrid.push(newListRow)
    }
    var numberOfRows = puzzleGrid.length
    var numberOfColumns = puzzleGrid[1].length
    puzzleGrid[numberOfRows - 1] = puzzleGrid[numberOfRows - 1].slice(0, numberOfColumns)
    // find the start and end position coordinates by enumerating across the puzzleSplit variable using list conditions, then cast them to the start and endCoords variables
    var startCoords = []
    for (let i = 0; i < numberOfRows; i++) {
        for (let j = 0; j < numberOfColumns; j++) {
            let startPosition = puzzleGrid[i][j]
            if (startPosition === "S") {
                startCoords.push(j, i)
            }

        }
    }
    var endCoords = []
    for (let i = 0; i < numberOfRows; i++) {
        for (let j = 0; j < numberOfColumns; j++) {
            let endPosition = puzzleGrid[i][j]
            if (endPosition === "E") {
                endCoords.push(j, i)
            }

        }
    }
    // convert the Start and End values to normal heights for us to turn into integers after using slice to grab the row values before the start / end, the replacement value
    // for the start / end, and then the row values after the start / end.
    puzzleGrid[startCoords[1]][startCoords[0]] = "a"
    puzzleGrid[endCoords[1]][endCoords[0]] = "z"
    // convert the heights from a-z into integers for us to work with by making a new list; I need a list of ints to make this easy work with - this is newGrid
    // We run a for loop on my earlier list of strings, converting them into values from 0-25 using letter.charCodeAt. then we push them to their row, and the row
    // to newGrid after the for loop runs on the row.
    for (let row of puzzleGrid) {
        let i = 0
        for (let letter of row) {
            letter = letter.replace(letter, letter.charCodeAt(0) - 97);
            row[i] = letter
            i++
        }
    }

    class DefaultDict {
        constructor(defaultValueFunc) {
            this.store = {};
            this.defaultValueFunc = defaultValueFunc;
        }

        get(key) {
            if (!(key in this.store)) {
                this.store[key] = this.defaultValueFunc();
            }
            return this.store[key];
        }

        set(key, value) {
            this.store[key] = value;
        }
    }

    var totalSteps = new DefaultDict(() => 1000000);
    totalSteps.set(startCoords, 0)
    var queue = [startCoords]
    function breadthFirstSearch(newGrid, queue) {
        while (queue.length > 0) {
            let currentLocation = queue.shift();
            if (currentLocation[0] === endCoords[0] && currentLocation[1] === endCoords[1]) {
                console.log(totalSteps.get(currentLocation))
                let answer = document.createElement("p")
                answer.className = "jozParagraph"
                answer.textContent = totalSteps.get(currentLocation)
                let jozDiv = document.querySelector('.jozDiv')
                jozDiv.appendChild(answer)
            }
            for (let direction of directions) {
                let nextStep = currentLocation.map((i, index) => i + Number(direction[index]))
                if (nextStep[0] > -1 && nextStep[0] < numberOfColumns && nextStep[1] > -1 && nextStep[1] < numberOfRows) {
                    let nextPiece = puzzleGrid[nextStep[1]][nextStep[0]]
                    if (nextPiece - puzzleGrid[currentLocation[1]][currentLocation[0]] <= 1) {
                        let currentSteps = +totalSteps.get(currentLocation) + 1
                        if (currentSteps < totalSteps.get(nextStep)) {
                            queue.push(nextStep)
                            totalSteps.set(nextStep, currentSteps)
                        }
                    }
                }
            }
        }
    }
    breadthFirstSearch(puzzleGrid, queue)
    var backwardsQueue = [endCoords]
    var pathBack = new Set()
    pathBack.add((JSON.stringify(endCoords)))
    function findPathBack(stepsToEndCoords, endCoords) {
        while (backwardsQueue.length > 0) {
            let currentLocation = backwardsQueue.shift()
            for (let direction of directions) {
                let previousStep = currentLocation.map((i, index) => i + Number(direction[index]))
                if (previousStep[0] > -1 && previousStep[0] < numberOfColumns && previousStep[1] > -1 && previousStep[1] < numberOfRows) {
                    let previousPiece = puzzleGrid[previousStep[1]][previousStep[0]]
                    if (puzzleGrid[currentLocation[1]][currentLocation[0]] - previousPiece <= 1) {
                        if (totalSteps.get(currentLocation) === totalSteps.get(previousStep) + 1) {
                            if (!pathBack.has(JSON.stringify(previousStep))) {
                                backwardsQueue.push(previousStep)
                                pathBack.add((JSON.stringify(previousStep)))
                            }
                        }
                    }

                }
            }
        }
        let jozDiv = document.querySelector(".jozDiv")
        let newPuzzle = document.createElement("p")
        for (let i = 0; i < numberOfRows; i++) {
            let currentRow = document.createElement("p")
            for (let j = 0; j < numberOfColumns; j++) {
                currentCoordinates = []
                currentCoordinates.push(j, i)
                if (pathBack.has(JSON.stringify(currentCoordinates))) {
                    let newColor = document.createElement("span");
                    newColor.textContent = puzzleSplit[i][j]
                    newColor.style.color = "white"
                    newColor.style.textAlign = "justify"
                    currentRow.append(newColor)
                } else {
                    let currentLetter = document.createElement("span");
                    currentLetter.textContent = puzzleSplit[i][j]
                    currentLetter.style.color = "black"
                    currentLetter.style.textAlign = "justify"
                    currentRow.append(currentLetter);
                }
                newPuzzle.style.textAlign = "justify"
                newPuzzle.append(currentRow)
            }
        }
        let oldPuzzle = document.querySelector(".jozPuzzle")
        console.log(oldPuzzle)
        jozDiv.removeChild(oldPuzzle)
        jozDiv.appendChild(newPuzzle)
    }
    findPathBack(totalSteps.get(endCoords), backwardsQueue)
})
