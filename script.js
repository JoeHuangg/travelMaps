const visitedStates = new Set();

function toggleState(stateId) {
    const stateElement = document.getElementById(`state-${stateId}`);
    if (visitedStates.has(stateId)) {
        visitedStates.delete(stateId);
        stateElement.classList.remove('visited');
    } else {
        visitedStates.add(stateId);
        stateElement.classList.add('visited');
    }
}

function downloadImage() {
    html2canvas(document.getElementById('map-container')).then(canvas => {
        const link = document.createElement('a');
        link.href = canvas.toDataURL();
        link.download = 'my-travel-map.png';
        link.click();
    });
}
