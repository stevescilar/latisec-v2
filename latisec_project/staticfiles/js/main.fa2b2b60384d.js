document.addEventListener("DOMContentLoaded", () => {
    const ctx = document.getElementById("securityChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Threat Detection", "Response Speed", "System Hardening"],
            datasets: [
                {
                    label: "Without Protection",
                    data: [52, 48, 59],
                    backgroundColor: "rgba(220, 53, 69, 0.7)",
                    borderRadius: 8
                },
                {
                    label: "With Latisec",
                    data: [92, 95, 89],
                    backgroundColor: "rgba(25, 135, 84, 0.8)",
                    borderRadius: 8
                }
            ]
        },
        options: {
            responsive: true,
            animation: {
                duration: 1500,
                easing: "easeOutQuart"
            },
            plugins: {
                legend: {
                    position: "bottom",
                    labels: {
                        font: { size: 14, weight: "500" }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: ctx => `${ctx.dataset.label}: ${ctx.raw}%`
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: value => value + "%"
                    }
                }
            }
        }
    });
});
