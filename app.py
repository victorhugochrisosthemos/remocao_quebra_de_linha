import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Texto sem quebra de linha",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        header, footer, [data-testid="stSidebar"] {
            display: none !important;
        }

        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        iframe {
            display: block !important;
        }

        .stApp {
            background: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
            overflow: hidden;
            font-family: Arial, Helvetica, sans-serif;
            background: #ffffff;
            color: #202124;
        }

        .app {
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
            background: #ffffff;
        }

        .content {
            flex: 1;
            display: grid;
            grid-template-columns: 1fr 1fr;
            min-height: 0;
            height: 100vh;
        }

        .panel {
            min-width: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .panel.left {
            background: #ffffff;
            border-right: 1px solid #dadce0;
        }

        .panel.right {
            background: #eef3fb;
        }

        .title-row {
            height: 50px;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 22px 0 62px;
            border-bottom: 1px solid #e0e0e0;
            background: inherit;
            font-size: 15px;
            color: #3c4043;
        }

        .clear-btn {
            border: none;
            background: transparent;
            color: #5f6368;
            font-size: 24px;
            cursor: pointer;
            line-height: 1;
        }

        .clear-btn:hover {
            color: #202124;
        }

        textarea {
            width: 100%;
            height: 100%;
            flex: 1;
            border: none;
            outline: none;
            resize: none;
            padding: 28px 62px;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 16px;
            line-height: 1.55;
            color: #3c4043;
            background: #ffffff;
            overflow-y: auto;
        }

        textarea::placeholder {
            color: #80868b;
        }

        .output {
            flex: 1;
            padding: 28px 76px;
            font-size: 16px;
            line-height: 1.55;
            color: #202124;
            overflow-y: auto;
            white-space: normal;
            overflow-wrap: break-word;
            background: #eef3fb;
        }

        .placeholder {
            color: #5f6368;
        }

        @media (max-width: 800px) {
            .content {
                grid-template-columns: 1fr;
                height: auto;
            }

            .panel.left,
            .panel.right {
                height: 50vh;
            }

            .title-row,
            textarea,
            .output {
                padding-left: 20px;
                padding-right: 20px;
            }
        }
        
        .copy-btn {
            border: none;
            background: transparent;
            font-size: 18px;
            cursor: pointer;
            color: #5f6368;
            margin-left: auto;
        }
        
        .copy-btn:hover {
            color: #202124;
        }

    </style>
</head>
<body>
    <div class="app">
        <div class="content">
            <section class="panel left">
                <div class="title-row">
                    <span>Texto original</span>
                    <button id="copyBtn" class="copy-btn" title="Copiar texto">📋</button>
                </div>

                <textarea
                    id="inputText"
                    placeholder="Cole seu texto aqui..."
                    autofocus
                ></textarea>
            </section>

            <section class="panel right">
                <div class="title-row">
                    <span>Resultado</span>
                </div>

                <div id="outputText" class="output placeholder">
                    Texto sem quebra de linha...
                </div>
            </section>
        </div>
    </div>

    <script>
        const input = document.getElementById("inputText");
        const output = document.getElementById("outputText");
        const clearBtn = document.getElementById("clearBtn");

        function removerQuebras(texto) {
            return texto.replace(/\\s*\\n\\s*/g, " ").trim();
        }

        function atualizarResultado() {
            const textoFinal = removerQuebras(input.value);

            if (textoFinal.length === 0) {
                output.textContent = "Cole um texto à esquerda para ver o resultado aqui.";
                output.classList.add("placeholder");
            } else {
                output.textContent = textoFinal;
                output.classList.remove("placeholder");
            }
        }

        input.addEventListener("input", atualizarResultado);

        clearBtn.addEventListener("click", function () {
            input.value = "";
            atualizarResultado();
            input.focus();
        });
        
        const copyBtn = document.getElementById("copyBtn");
        
        copyBtn.addEventListener("click", async function () {
            const texto = output.textContent;
        
            if (!texto || texto.includes("Cole um texto")) return;
        
            try {
                await navigator.clipboard.writeText(texto);
        
                copyBtn.textContent = "✅";
                setTimeout(() => {
                    copyBtn.textContent = "📋";
                }, 1200);

    </script>
</body>
</html>
"""

components.html(html_code, height=720, scrolling=False)
