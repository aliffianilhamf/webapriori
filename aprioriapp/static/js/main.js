(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    // Progress Bar
    $('.pg-bar').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: true,
        loop: true,
        nav : false
    });


    // Worldwide Sales Chart
    // var ctx1 = $("#worldwide-sales").get(0).getContext("2d");
    // var myChart1 = new Chart(ctx1, {
    //     type: "bar",
    //     data: {
    //         labels: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    //         datasets: [{
    //                 label: "USA",
    //                 data: [15, 30, 55, 65, 60, 80, 95],
    //                 backgroundColor: "rgba(0, 156, 255, .7)"
    //             },
    //             {
    //                 label: "UK",
    //                 data: [8, 35, 40, 60, 70, 55, 75],
    //                 backgroundColor: "rgba(0, 156, 255, .5)"
    //             },
    //             {
    //                 label: "AU",
    //                 data: [12, 25, 45, 55, 65, 70, 60],
    //                 backgroundColor: "rgba(0, 156, 255, .3)"
    //             }
    //         ]
    //         },
    //     options: {
    //         responsive: true
    //     }
    // });


    //Salse & Revenue Chart
    // var ctx2 = $("#salse-revenue").get(0).getContext("2d");
    // var myChart2 = new Chart(ctx2, {
    //     type: "line",
    //     data: {
    //         labels: ["2016", "2017", "2018", "2019", "2020", "2021", "2022"],
    //         datasets: [{
    //                 label: "Salse",
    //                 data: [15, 30, 55, 45, 70, 65, 85],
    //                 backgroundColor: "rgba(0, 156, 255, .5)",
    //                 fill: true
    //             },
    //             {
    //                 label: "Revenue",
    //                 data: [99, 135, 170, 130, 190, 180, 270],
    //                 backgroundColor: "rgba(0, 156, 255, .3)",
    //                 fill: true
    //             }
    //         ]
    //         },
    //     options: {
    //         responsive: true
    //     }
    // });
    


    // Single Line Chart
    // var ctx3 = $("#line-chart").get(0).getContext("2d");
    // var myChart3 = new Chart(ctx3, {
    //     type: "line",
    //     data: {
    //         labels: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    //         datasets: [{
    //             label: "Salse",
    //             fill: false,
    //             backgroundColor: "rgba(0, 156, 255, .3)",
    //             data: [7, 8, 8, 9, 9, 9, 10, 11, 14, 14, 15]
    //         }]
    //     },
    //     options: {
    //         responsive: true
    //     }
    // });


    // // Single Bar Chart
    // var ctx4 = $("#bar-chart").get(0).getContext("2d");
    // var myChart4 = new Chart(ctx4, {
    //     type: "bar",
    //     data: {
    //         labels: ["Italy", "France", "Spain", "USA", "Argentina"],
    //         datasets: [{
    //             backgroundColor: [
    //                 "rgba(0, 156, 255, .7)",
    //                 "rgba(0, 156, 255, .6)",
    //                 "rgba(0, 156, 255, .5)",
    //                 "rgba(0, 156, 255, .4)",
    //                 "rgba(0, 156, 255, .3)"
    //             ],
    //             data: [55, 49, 44, 24, 15]
    //         }]
    //     },
    //     options: {
    //         responsive: true
    //     }
    // });


    // // Pie Chart
    // var ctx5 = $("#pie-chart").get(0).getContext("2d");
    // var myChart5 = new Chart(ctx5, {
    //     type: "pie",
    //     data: {
    //         labels: ["Italy", "France", "Spain", "USA", "Argentina"],
    //         datasets: [{
    //             backgroundColor: [
    //                 "rgba(0, 156, 255, .7)",
    //                 "rgba(0, 156, 255, .6)",
    //                 "rgba(0, 156, 255, .5)",
    //                 "rgba(0, 156, 255, .4)",
    //                 "rgba(0, 156, 255, .3)"
    //             ],
    //             data: [55, 49, 44, 24, 15]
    //         }]
    //     },
    //     options: {
    //         responsive: true
    //     }
    // });


    // // Doughnut Chart
    // var ctx6 = $("#doughnut-chart").get(0).getContext("2d");
    // var myChart6 = new Chart(ctx6, {
    //     type: "doughnut",
    //     data: {
    //         labels: ["Italy", "France", "Spain", "USA", "Argentina"],
    //         datasets: [{
    //             backgroundColor: [
    //                 "rgba(0, 156, 255, .7)",
    //                 "rgba(0, 156, 255, .6)",
    //                 "rgba(0, 156, 255, .5)",
    //                 "rgba(0, 156, 255, .4)",
    //                 "rgba(0, 156, 255, .3)"
    //             ],
    //             data: [55, 49, 44, 24, 15]
    //         }]
    //     },
    //     options: {
    //         responsive: true
    //     }
    // });
   



    // chart 1
    fetch('chart_data/')
    .then(response => response.json())
    .then(data => {
        // Verify that the element exists
        var ctx1 = $("#transaksi_paling_laris");
        if (ctx1.length === 0) {
            console.error("Element with ID 'transaksi_paling_laris' not found.");
            return;
        }
        var myChart1 = new Chart(ctx1.get(0).getContext("2d"), {
            type: "line",
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Item Name",
                    data: data.data,
                    backgroundColor: [
                        'rgba(0, 156, 255, .3)', '#A52A2A',
                        '#FF6347', '#FF69B4', '#FF1493', '#DA70D6', '#800080', '#4B0082',
                        '#0000FF', '#1E90FF', '#00BFFF', '#00CED1', '#20B2AA', '#008B8B'
                    ],
                    borderColor: 'lime',
                    fill: true
                }]
            },
            options: {
                responsive: true
            }
        });


    })
    .catch(error => {
        console.error('Error fetching or parsing data:', error);
    });

    //chart2
    fetch('transaksi_tiap_bulan/')
    .then(response => response.json())
    .then(data => {
        // Verify that the element exists
        var ctx2 = $("#transaksi_tiap_bulan");
        if (ctx2.length === 0) {
            console.error("Element with ID 'transaksi_tiap_bulan' not found.");
            return;
        }
        var myChart2 = new Chart(ctx2.get(0).getContext("2d"), {
            type: "pie",
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Month",
                    data: data.data,
                    backgroundColor: ["grey","brown","#90EE90","navy","coral","#6495ED","#BDB76B","salmon","#FF1493","#FFD700","lime","red"],
                    fill: true
                }]
            },
            options: {
                responsive: true
            }
        });


    })
    .catch(error => {
        console.error('Error fetching or parsing data:', error);
    });


    // chart 3
    fetch('transaksi_per_hari/')
    .then(response => response.json())
    .then(data => {
        // Verify that the element exists
        var ctx3 = $("#transaksi_per_hari");
        if (ctx3.length === 0) {
            console.error("Element with ID 'transaksi_per_hari' not found.");
            return;
        }
        var myChart3 = new Chart(ctx3.get(0).getContext("2d"), {
            type: "doughnut",
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Day",
                    data: data.data,
                    backgroundColor: ["red", "green","blue","orange","brown","purple","pink"],
                    fill: true
                }]
            },
            options: {
                display: true,
                responsive: true
            }
        });


    })
    .catch(error => {
        console.error('Error fetching or parsing data:', error);
    });
    // chart 3
    fetch('transaksi_per_jam/')
    .then(response => response.json())
    .then(data => {
        // Verify that the element exists
        var ctx4 = $("#transaksi_per_jam");
        if (ctx4.length === 0) {
            console.error("Element with ID 'transaksi_per_jam' not found.");
            return;
        }
        var myChart4 = new Chart(ctx4.get(0).getContext("2d"), {
            type: "bar",
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Hour",
                    data: data.data,
                    backgroundColor: [
                        '#FF0000', '#FF4500', '#FF8C00', '#FFD700', '#FFFF00', '#ADFF2F',
                        '#7FFF00', '#32CD32', '#008000', '#006400', '#8B4513', '#A52A2A',
                        '#FF6347', '#FF69B4', '#FF1493', '#DA70D6', '#800080', '#4B0082',
                        '#0000FF', '#1E90FF', '#00BFFF', '#00CED1', '#20B2AA', '#008B8B'
                    ],
                    fill: true
                }]
            },
            options: {
                responsive: true
            }
        });


    })
    .catch(error => {
        console.error('Error fetching or parsing data:', error);
    });

    
})(jQuery);

