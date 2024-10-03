import streamlit as st
import dataclasses
import helper_functions
import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

helper_functions.load_widget_state()

if "suspect" not in st.session_state:
    st.session_state["suspect"] = ""
if "pic_disabled" not in st.session_state:
    st.session_state["pic_disabled"] = False
if "results_disabled" not in st.session_state:
    st.session_state["results_disabled"] = False




# [start] ____________________________________________________

def check_suspect():
    st.markdown("""
        <style>
        .main .block-container {
            max-width: 90%;  /* Set to 100% for full width, or adjust (90% for slightly smaller) */
            padding-left: 5%;
            padding-right: 5%;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        h1 {
            border-bottom: 7px solid #004182;  /* White line underneath */
            padding-bottom: 5px;            /* Add some space between the text and the line */
        }
        </style>
        """, unsafe_allow_html=True)

    # Set the background and text color as you did earlier
    st.markdown("""
        <style>
        .stApp {
            background-color: white;  /* Dark grey background */
        }
        h1, h2, h3, h4, h5, h6, p, li, span, div {
            color: #004182;  /* White text color */
        }
        </style>
        """, unsafe_allow_html=True)

    st.title('Politie Verdachtencheck :cop:')
    st.write('')
    st.write('')


    st.logo("assets/politie_logo.svg")

    annemarie = ["ANNEMARIE", "ANEMARIE", "ANNE", "ANNE MARIE", "ANNE-MARIE", "A-M"]
    meyke = ["MEYKE", "MAYKE"]
    ben = ["BEN", "BEEN", "BAN"]
    ivo = ["IVO", "YVO", "IVVO"]
    meike = ["MEIKE", "MEIKE", "MAIKE"]
    loes = ["LOES"]
    isabel = ["ISABEL", "ISAEL", "ISABELLE"]
    detectives = ["DETECTIVES", "DETECTIVE", "THE DETECTIVES", "DE DETECTIVES"]
    flamingos = ["FLAMINGOS", "FLAMINGO'S"]
    uilenspionnen = ["UILENSPIONNEN", "UILESPIONNEN", "UILEN SPIONNEN", "UILE SPIONNEN"]
    gang = ["DETECTIVE GANG", "DETECTIVE-GANG", "GANG"]


    st.text_input(
            f"Voer de naam van de verdachte in 👇",
            type="default",
            placeholder="naam",
            value='',
            key='suspect'
        )

    if st.session_state.suspect == "":
        st.warning("**Voer een naam in!**")
        return  # Exit early if the input is empty

    suspect_upper = st.session_state.suspect.upper()

    st.checkbox("Foto uploaden", key="pic_disabled")

    if st.session_state.pic_disabled:

        picture = st.camera_input(
            "Take a picture",
        )


    progress_text = "Check Database. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    col1, col2 = st.columns(2)

    ###############################################################
    # ANNEMARIE
    ###############################################################
    if suspect_upper in annemarie:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.59841],
                'lon': [5.32082, 5.31619],
                'color': ['#004182', '#c30010']
            }

            # Create the DataFrame
            df = pd.DataFrame(data)

            # Plot the map
            st.map(df, color='color', size=50, zoom=10)

            code = '''Afstand tot plaats delict: 1120 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["verdachte activiteiten", "DNA", "sporenonderzoek"])

            st.area_chart(chart_data, height=600)


    ###############################################################
    # MEYKE
    ###############################################################
    elif suspect_upper in meyke:

        with col1:
            st.header("Alibi")
            start_lat = 51.60785  # Replace with your latitude
            start_lon = 5.32082  # Replace with your longitude
            df = pd.DataFrame(
                np.random.randn(100, 2) / [50, 50] + [start_lat, start_lon],
                columns=["lat", "lon"],
            )
            st.map(df)

            code = '''Afstand tot plaats delict: 5-18763 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            chart_data = pd.DataFrame(np.random.randn(100, 2), columns=["Forensisch onderzoek", "Bewijsmateriaal"])
            words = ["oorzaak", "aanleiding", "punten"]
            chart_data["Sectie"] = [random.choice(words) for _ in range(100)]

            st.vega_lite_chart(
                chart_data,
                {
                    "mark": "point",
                    "encoding": {
                        "x": {"field": "Forensisch onderzoek", "type": "quantitative"},
                        "y": {"field": "Bewijsmateriaal", "type": "quantitative"},
                        "size": {"field": "Sectie", "type": "nominal"},
                        "color": {"field": "Sectie", "type": "nominal"},
                        "shape": {"field": "Sectie", "type": "nominal"},
                    },
                },
                use_container_width=True
            )


    ###############################################################
    # ISABEL
    ###############################################################
    elif suspect_upper in isabel:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            fig, ax = plt.subplots(figsize=(6, 6))

            nx = 101
            ny = 105

            # Set up survey vectors
            xvec = np.linspace(0.001, 4.0, nx)
            yvec = np.linspace(0.001, 4.0, ny)

            # Set up survey matrices.  Design disk loading and gear ratio.
            x1, x2 = np.meshgrid(xvec, yvec)

            # Evaluate some stuff to plot
            obj = x1 ** 2 + x2 ** 2 - 2 * x1 - 2 * x2 + 2
            g1 = -(3 * x1 + x2 - 5.5)
            g2 = -(x1 + 2 * x2 - 4.5)
            g3 = 0.8 + x1 ** -3 - x2

            cntr = ax.contour(x1, x2, obj, [0.01, 0.1, 0.5, 1, 2, 4, 8, 16],
                              colors='black')
            ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)

            cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')
            cg1.set(path_effects=[patheffects.withTickedStroke(angle=135)])

            cg2 = ax.contour(x1, x2, g2, [0], colors='orangered')
            cg2.set(path_effects=[patheffects.withTickedStroke(angle=60, length=2)])

            cg3 = ax.contour(x1, x2, g3, [0], colors='mediumblue')
            cg3.set(path_effects=[patheffects.withTickedStroke(spacing=7)])

            ax.set_xlim(0, 4)
            ax.set_ylim(0, 4)

            st.pyplot(fig)



    ###############################################################
    # BEN
    # @ Meyke nog map aanpassen
    ###############################################################
    elif suspect_upper in ben:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            def hat_graph(ax, xlabels, values, group_labels):
                def label_bars(heights, rects):
                    """Attach a text label on top of each bar."""
                    for height, rect in zip(heights, rects):
                        ax.annotate(f'{height}',
                                    xy=(rect.get_x() + rect.get_width() / 2, height),
                                    xytext=(0, 4),  # 4 points vertical offset.
                                    textcoords='offset points',
                                    ha='center', va='bottom')

                values = np.asarray(values)
                x = np.arange(values.shape[1])
                ax.set_xticks(x, labels=xlabels)
                spacing = 0.3  # spacing between hat groups
                width = (1 - spacing) / values.shape[0]
                heights0 = values[0]
                for i, (heights, group_label) in enumerate(zip(values, group_labels)):
                    style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
                    rects = ax.bar(x - spacing / 2 + i * width, heights - heights0,
                                   width, bottom=heights0, label=group_label, **style)
                    label_bars(heights, rects)

            # initialise labels and a numpy array make sure you have
            # N labels of N number of values in the array
            xlabels = ['I', 'II', 'III', 'IV', 'V']
            playerA = np.array([5, 15, 22, 20, 25])
            playerB = np.array([25, 32, 34, 30, 27])

            fig, ax = plt.subplots()
            hat_graph(ax, xlabels, [playerA, playerB], ['bewijskracht', 'scherpte'])

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_xlabel('afdruk')
            ax.set_ylabel('Score')
            ax.set_ylim(0, 60)
            ax.set_title('Vingerafdrukanalyse')
            ax.legend()

            fig.tight_layout()

            st.pyplot(fig)



    ###############################################################
    # IVO
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in ivo:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")
            chart_data = pd.DataFrame(np.random.randn(20, 3),
                                      columns=["Profielschets", "Forensische sporen", "Observatie resultaten"])

            st.area_chart(chart_data, height=600, color=['#FF5733', '#33C1FF', '#8D33FF'])



    ###############################################################
    # LOES
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in loes:

        with col1:
            st.header("Alibi")
            start_lat = 51.60785  # Replace with your latitude
            start_lon = 5.32082  # Replace with your longitude
            df = pd.DataFrame(
                np.random.randn(100, 2) / [50, 50] + [start_lat, start_lon],
                columns=["lat", "lon"],
            )
            st.map(df)

            code = '''Afstand tot plaats delict: 5-18763 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            chart_data = pd.DataFrame(np.random.randn(25, 2),
                                      columns=["Getuigenverhoor", "Technisch recherchewerk"])
            words = ["buitenlandse", "binnenlandse"]
            chart_data["Inlichtingen"] = [random.choice(words) for _ in range(25)]

            st.vega_lite_chart(
                chart_data,
                {
                    "mark": "point",
                    "encoding": {
                        "x": {"field": "Getuigenverhoor", "type": "quantitative"},
                        "y": {"field": "Technisch recherchewerk", "type": "quantitative"},
                        "size": {"field": "Inlichtingen", "type": "nominal"},
                        "color": {"field": "Inlichtingen", "type": "nominal"},
                    },
                },
                use_container_width=True
            )




    ###############################################################
    # Meike
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in meike:

        with col1:
            st.header("Alibi")
            start_lat = 51.60785
            start_lon = 5.32082
            df = pd.DataFrame(
                np.random.randn(2, 2) / [50, 50] + [start_lat, start_lon],
                columns=["lat", "lon"],
            )
            st.map(df)

            code = '''Afstand tot plaats delict: 5-18763 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["voortgang deel A", "voortgang deel B", "voortgang deel C"])

            st.bar_chart(chart_data, height=600)

    ###############################################################
    # Detectives
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in detectives:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            chart_data = pd.DataFrame(np.random.randn(20, 5),
                                      columns=["Jorn", "Ytse", "Rowan", "Rehan", "Djairo"])

            st.bar_chart(chart_data, height=600)

    ###############################################################
    # Flamingo
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in flamingos:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Activiteiten")

            chart_data = pd.DataFrame(np.random.randn(25, 2),
                                      columns=["Getuigenverhoor", "Technisch recherchewerk"])
            words = ["Lina", "Ouassin", "Ronin", "Guusje"]
            chart_data["Inlichtingen"] = [random.choice(words) for _ in range(25)]

            st.vega_lite_chart(
                chart_data,
                {
                    "mark": "point",
                    "encoding": {
                        "x": {"field": "Getuigenverhoor", "type": "quantitative"},
                        "y": {"field": "Technisch recherchewerk", "type": "quantitative"},
                        "size": {"field": "Inlichtingen", "type": "nominal"},
                        "color": {"field": "Inlichtingen", "type": "nominal"},
                    },
                },
                use_container_width=True
            )

    ###############################################################
    # Gang
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in gang:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Inlichtingen")

            chart_data = pd.DataFrame(np.random.randn(20, 5),
                                      columns=["Bes", "Veerle", "Tijs", "Thaniel", "Niels"])

            st.bar_chart(chart_data, height=600)

    ###############################################################
    # Uilenspionnen
    # @ Meyke map aanpassen
    ###############################################################
    elif suspect_upper in uilenspionnen:

        with col1:
            st.header("Alibi")
            data = {
                'lat': [51.60785, 51.60785],
                'lon': [5.32082, 5.32082],
                'color': ['#004182', '#c30010'],
                'size': [100, 10]
            }

            # Create the DataFrame
            df = pd.DataFrame(data)
            st.map(df, color='color', size='size', zoom=14)

            code = '''Afstand tot plaats delict: 0 meter'''
            st.code(code, language="python")

        with col2:
            st.header("Inlichtingen")

            chart_data = pd.DataFrame(np.random.randn(25, 2),
                                      columns=["Getuigenverhoor", "Technisch recherchewerk"])
            words = ["Julie", "Ben", "Lizzy", "Jasper", "David"]
            chart_data["Inlichtingen"] = [random.choice(words) for _ in range(25)]

            st.vega_lite_chart(
                chart_data,
                {
                    "mark": "point",
                    "encoding": {
                        "x": {"field": "Getuigenverhoor", "type": "quantitative"},
                        "y": {"field": "Technisch recherchewerk", "type": "quantitative"},
                        "size": {"field": "Inlichtingen", "type": "nominal"},
                        "color": {"field": "Inlichtingen", "type": "nominal"},
                    },
                },
                use_container_width=True
            )

    else:
        st.write('Dit is geen verdachte in het onderzoek naar het verdwenen fosiel.')

    @st.dialog("Resultaten Onderzoek")
    def result(hm_suspect):
        st.write(f"Onderbroeksresultaat voor {hm_suspect}:")

        # Display the appropriate image based on the suspect
        if suspect_upper in annemarie:
            st.image("assets/Annemarie.png")
        elif suspect_upper in meyke:
            st.image("assets/Meyke.png")
        elif suspect_upper in isabel:
            st.image("assets/isabel.png")
        elif suspect_upper in ben:
            st.image("assets/geen_afbeelding.png")
        elif suspect_upper in ivo:
            st.image("assets/Ivo.png")
        elif suspect_upper in loes:
            st.image("assets/Loes.png")
        elif suspect_upper in meike:
            st.image("assets/geen_afbeelding.png")
        elif suspect_upper in uilenspionnen:
            st.image("assets/uilenspionnen.png")
        elif suspect_upper in gang:
            st.image("assets/detective_gang.png")
        elif suspect_upper in detectives:
            st.image("assets/detectives.png")
        elif suspect_upper in flamingos:
            st.image("assets/flamingos.png")

    st.session_state.results_disabled = st.toggle("Show resultaten", value=st.session_state.results_disabled)
    if st.session_state.results_disabled:
        result(st.session_state.suspect)


    if st.button("Reset - Check een nieuwe verdachte"):
        # Clear the session state
        st.session_state.clear()
        st.session_state.suspect = ""
        st.session_state.results_disabled = False
        st.session_state.pic_disabled = False

        # Rerun the app
        st.rerun()








if __name__ == "__main__":
    check_suspect()


