function createChartDisease(diseases, counts ) {
    const ctx = document.getElementById('diseaseChart').getContext('2d');
    const chart = new Chart(ctx, {
        // Basis des Charts
        type: 'bar',
        data: {
            labels: diseases,
            datasets: [{
                data: counts,
                backgroundColor: ['#ff6384', '#36a2eb', '#cc65fe', '#ffce56', '#2eb82e', '#2e33b8', '#b82e2e'],
                hoverBackgroundColor: ['#ff6384', '#36a2eb', '#cc65fe', '#ffce56', '#2eb82e', '#2e33b8', '#b82e2e']
            }]
        },
    });
}