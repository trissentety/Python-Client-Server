

< !DOCTYPE html >
    <html>

        <head>
            <title>DOM console.log() Method</title>
            <style>
                h1 {
                    color: green;
        }

                h2 {
                    font - family: Impact;
        }

                body {
                    text - align: center;
        }
            </style>
        </head>

        <body>
            <h1>GeeksforGeeks</h1>
            <h2>DOM console.log() Method</h2>
            <p>
                To view the message in the console
                press the F12 key on your keyboard.
            </p>
            <p>
                To view the message, double click
                the button below:
            </p>
            <br>
                <button ondblclick="log_console()">
                    View Message
                </button>
                <script>
                    function log_console() {
                        console.log
                            ("GeeksforGeeks is a portal for geeks.");
        }
                </script>
        </body>

    </html>