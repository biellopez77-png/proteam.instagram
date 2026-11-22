#!/usr/bin/env python3
"""T-04 / mejora continua (traducciones): páginas públicas (blog, biblioteca de
ejercicios y plantilla gratis) salían en castellano en en, fr, pt, de e it.

En `src/lib/i18n/dict/{en,fr,pt,de,it}.json` estas 45 claves tienen como valor el
mismo texto castellano (ca sí está traducido). `i18n-check` no lo detecta porque
solo exige un valor no vacío. Este script rellena SOLO las claves cuyo valor
sigue siendo idéntico a la clave; no toca nada más, conserva el orden y el
final de archivo.

Uso (en la raíz de proteamapp):  python3 aplicar.py && bun run build
"""
import json, pathlib, sys

T = {
"¡Tu plantilla está lista!": dict(en="Your template is ready!", fr="Votre modèle est prêt !", pt="O seu modelo está pronto!", de="Deine Vorlage ist fertig!", it="Il tuo modello è pronto!"),
"2x2 desde bloqueo directo": dict(en="2v2 from a direct screen", fr="2x2 à partir d'un écran direct", pt="2x2 a partir de bloqueio direto", de="2-gegen-2 aus dem direkten Block", it="2 contro 2 dal blocco diretto"),
"3x3 con transición a contraataque": dict(en="3v3 with transition to counter-attack", fr="3x3 avec transition en contre-attaque", pt="3x3 com transição para contra-ataque", de="3-gegen-3 mit Umschalten in den Gegenstoß", it="3 contro 3 con transizione in contropiede"),
"4 noviembre 2026": dict(en="4 November 2026", fr="4 novembre 2026", pt="4 de novembro de 2026", de="4. November 2026", it="4 novembre 2026"),
"Acepto recibir la plantilla y emails de ProTeam con consejos de entrenamiento; puedo darme de baja cuando quiera": dict(
    en="I agree to receive the template and ProTeam emails with training tips; I can unsubscribe at any time",
    fr="J'accepte de recevoir le modèle et des e-mails de ProTeam avec des conseils d'entraînement ; je peux me désabonner à tout moment",
    pt="Aceito receber o modelo e emails da ProTeam com dicas de treino; posso cancelar a subscrição quando quiser",
    de="Ich möchte die Vorlage und E-Mails von ProTeam mit Trainingstipps erhalten; ich kann mich jederzeit abmelden",
    it="Accetto di ricevere il modello ed email di ProTeam con consigli di allenamento; posso disiscrivermi quando voglio"),
"Artículo no encontrado | ProTeam App": dict(en="Article not found | ProTeam App", fr="Article introuvable | ProTeam App", pt="Artigo não encontrado | ProTeam App", de="Artikel nicht gefunden | ProTeam App", it="Articolo non trovato | ProTeam App"),
"Balonmano, baloncesto y fútbol: objetivos claros, situaciones de juego y claves de entrenamiento.": dict(
    en="Handball, basketball and football: clear objectives, game situations and coaching keys.",
    fr="Handball, basket-ball et football : objectifs clairs, situations de jeu et clés d'entraînement.",
    pt="Andebol, basquetebol e futebol: objetivos claros, situações de jogo e chaves de treino.",
    de="Handball, Basketball und Fußball: klare Ziele, Spielsituationen und Trainingsschwerpunkte.",
    it="Pallamano, pallacanestro e calcio: obiettivi chiari, situazioni di gioco e chiavi di allenamento."),
"Biblioteca pública de ejercicios con objetivos, desarrollo y claves para entrenar equipos de formación.": dict(
    en="Public exercise library with objectives, setup and coaching keys for youth teams.",
    fr="Bibliothèque publique d'exercices avec objectifs, déroulement et clés pour entraîner les équipes de formation.",
    pt="Biblioteca pública de exercícios com objetivos, desenvolvimento e chaves para treinar equipas de formação.",
    de="Öffentliche Übungsbibliothek mit Zielen, Ablauf und Trainingsschwerpunkten für Nachwuchsteams.",
    it="Biblioteca pubblica di esercizi con obiettivi, svolgimento e chiavi per allenare le squadre giovanili."),
"Blog de entrenamiento y planificación deportiva | ProTeam App": dict(en="Training and sports planning blog | ProTeam App", fr="Blog d'entraînement et de planification sportive | ProTeam App", pt="Blog de treino e planeamento desportivo | ProTeam App", de="Blog zu Training und Trainingsplanung | ProTeam App", it="Blog di allenamento e pianificazione sportiva | ProTeam App"),
"Carga = RPE × minutos. Los datos son ejemplos editables. Los indicadores de carga son orientativos y no sustituyen una valoración profesional.": dict(
    en="Load = RPE × minutes. The data are editable examples. Load indicators are a guide and do not replace a professional assessment.",
    fr="Charge = RPE × minutes. Les données sont des exemples modifiables. Les indicateurs de charge sont indicatifs et ne remplacent pas une évaluation professionnelle.",
    pt="Carga = RPE × minutos. Os dados são exemplos editáveis. Os indicadores de carga são orientativos e não substituem uma avaliação profissional.",
    de="Belastung = RPE × Minuten. Die Daten sind bearbeitbare Beispiele. Die Belastungswerte dienen nur zur Orientierung und ersetzen keine fachliche Beurteilung.",
    it="Carico = RPE × minuti. I dati sono esempi modificabili. Gli indicatori di carico sono orientativi e non sostituiscono una valutazione professionale."),
"Circulación contra 6:0 con cruce": dict(en="Ball circulation against 6:0 with a crossing", fr="Circulation contre 6:0 avec croisé", pt="Circulação contra 6:0 com cruzamento", de="Ballzirkulation gegen 6:0 mit Kreuzen", it="Circolazione contro 6:0 con incrocio"),
"Claves del entrenador": dict(en="Coaching keys", fr="Clés de l'entraîneur", pt="Chaves do treinador", de="Hinweise für den Trainer", it="Chiavi dell'allenatore"),
"Cómo medir y controlar la carga de entrenamiento en un equipo de baloncesto de formación usando RPE, sin GPS ni material caro.": dict(
    en="How to measure and control training load in a youth basketball team using RPE, without GPS or expensive equipment.",
    fr="Comment mesurer et contrôler la charge d'entraînement d'une équipe de basket de formation avec le RPE, sans GPS ni matériel coûteux.",
    pt="Como medir e controlar a carga de treino numa equipa de basquetebol de formação com RPE, sem GPS nem material caro.",
    de="Wie du die Trainingsbelastung in einem Nachwuchs-Basketballteam mit RPE misst und steuerst – ohne GPS oder teure Ausrüstung.",
    it="Come misurare e controllare il carico di allenamento in una squadra giovanile di pallacanestro con l'RPE, senza GPS né materiale costoso."),
"Cómo planificar una temporada de balonmano juvenil (con plantilla gratis)": dict(en="How to plan a youth handball season (with a free template)", fr="Comment planifier une saison de handball jeunes (avec modèle gratuit)", pt="Como planear uma época de andebol juvenil (com modelo grátis)", de="So planst du eine Saison im Jugendhandball (mit kostenloser Vorlage)", it="Come pianificare una stagione di pallamano giovanile (con modello gratuito)"),
"Control de carga en baloncesto de formación: guía sencilla con RPE": dict(en="Load control in youth basketball: a simple RPE guide", fr="Contrôle de la charge en basket de formation : guide simple avec le RPE", pt="Controlo de carga no basquetebol de formação: guia simples com RPE", de="Belastungssteuerung im Nachwuchsbasketball: einfacher Leitfaden mit RPE", it="Controllo del carico nella pallacanestro giovanile: guida semplice con l'RPE"),
"Descarga gratis una plantilla Excel con Jugadores, Temporada, Sesiones y Resumen para planificar tu equipo y controlar la carga RPE.": dict(
    en="Download a free Excel template with Players, Season, Sessions and Summary to plan your team and track RPE load.",
    fr="Téléchargez gratuitement un modèle Excel avec Joueurs, Saison, Séances et Résumé pour planifier votre équipe et suivre la charge RPE.",
    pt="Descarregue grátis um modelo Excel com Jogadores, Época, Sessões e Resumo para planear a sua equipa e controlar a carga RPE.",
    de="Lade kostenlos eine Excel-Vorlage mit Spieler, Saison, Einheiten und Zusammenfassung herunter, um dein Team zu planen und die RPE-Belastung zu steuern.",
    it="Scarica gratis un modello Excel con Giocatori, Stagione, Sessioni e Riepilogo per pianificare la tua squadra e controllare il carico RPE."),
"Descarga tu plantilla gratuita.": dict(en="Download your free template.", fr="Téléchargez votre modèle gratuit.", pt="Descarregue o seu modelo gratuito.", de="Lade deine kostenlose Vorlage herunter.", it="Scarica il tuo modello gratuito."),
"Descargar plantilla gratis": dict(en="Download free template", fr="Télécharger le modèle gratuit", pt="Descarregar modelo grátis", de="Kostenlose Vorlage herunterladen", it="Scarica il modello gratuito"),
"Ejercicio no encontrado | ProTeam App": dict(en="Exercise not found | ProTeam App", fr="Exercice introuvable | ProTeam App", pt="Exercício não encontrado | ProTeam App", de="Übung nicht gefunden | ProTeam App", it="Esercizio non trovato | ProTeam App"),
"Ejercicios de balonmano, baloncesto y fútbol | ProTeam App": dict(en="Handball, basketball and football exercises | ProTeam App", fr="Exercices de handball, basket-ball et football | ProTeam App", pt="Exercícios de andebol, basquetebol e futebol | ProTeam App", de="Übungen für Handball, Basketball und Fußball | ProTeam App", it="Esercizi di pallamano, pallacanestro e calcio | ProTeam App"),
"Ejercicios para llevar a la pista": dict(en="Exercises to take to the court", fr="Des exercices à emmener sur le terrain", pt="Exercícios para levar para o campo", de="Übungen für die Halle", it="Esercizi da portare in campo"),
"Filtrar por deporte": dict(en="Filter by sport", fr="Filtrer par sport", pt="Filtrar por desporto", de="Nach Sportart filtern", it="Filtra per sport"),
"Guía práctica para planificar la temporada de un equipo de balonmano juvenil por mesociclos y microciclos, con control de carga y plantilla descargable.": dict(
    en="A practical guide to planning a youth handball team's season by mesocycles and microcycles, with load control and a downloadable template.",
    fr="Guide pratique pour planifier la saison d'une équipe de handball jeunes par mésocycles et microcycles, avec contrôle de la charge et modèle téléchargeable.",
    pt="Guia prático para planear a época de uma equipa de andebol juvenil por mesociclos e microciclos, com controlo de carga e modelo para descarregar.",
    de="Praxisleitfaden, um die Saison eines Jugendhandballteams in Meso- und Mikrozyklen zu planen – mit Belastungssteuerung und Vorlage zum Herunterladen.",
    it="Guida pratica per pianificare la stagione di una squadra di pallamano giovanile per mesocicli e microcicli, con controllo del carico e modello scaricabile."),
"Guías prácticas de planificación, control de carga y entrenamiento para balonmano, baloncesto y fútbol.": dict(
    en="Practical guides on planning, load control and training for handball, basketball and football.",
    fr="Guides pratiques de planification, de contrôle de la charge et d'entraînement pour le handball, le basket-ball et le football.",
    pt="Guias práticos de planeamento, controlo de carga e treino para andebol, basquetebol e futebol.",
    de="Praxisleitfäden zu Planung, Belastungssteuerung und Training für Handball, Basketball und Fußball.",
    it="Guide pratiche di pianificazione, controllo del carico e allenamento per pallamano, pallacanestro e calcio."),
"Guías prácticas para el día a día de entrenadores y equipos de formación.": dict(
    en="Practical guides for the day-to-day of coaches and youth teams.",
    fr="Guides pratiques pour le quotidien des entraîneurs et des équipes de formation.",
    pt="Guias práticos para o dia a dia de treinadores e equipas de formação.",
    de="Praxisleitfäden für den Alltag von Trainern und Nachwuchsteams.",
    it="Guide pratiche per il quotidiano di allenatori e squadre giovanili."),
"Juego de posición 5x5+3": dict(en="5v5+3 positional game", fr="Jeu de position 5x5+3", pt="Jogo de posição 5x5+3", de="Positionsspiel 5-gegen-5+3", it="Gioco di posizione 5 contro 5+3"),
"La descarga ha comenzado. Ya puedes adaptarla a tu equipo.": dict(en="Your download has started. You can now adapt it to your team.", fr="Le téléchargement a commencé. Vous pouvez maintenant l'adapter à votre équipe.", pt="A transferência começou. Já pode adaptá-lo à sua equipa.", de="Der Download hat begonnen. Du kannst sie jetzt an dein Team anpassen.", it="Il download è iniziato. Ora puoi adattarlo alla tua squadra."),
"Llévalo a tu equipo con ProTeam App": dict(en="Take it to your team with ProTeam App", fr="Emmenez-le dans votre équipe avec ProTeam App", pt="Leve-o para a sua equipa com a ProTeam App", de="Bring es mit ProTeam App in dein Team", it="Portalo nella tua squadra con ProTeam App"),
"No se ha podido preparar el archivo. Recarga la página para reintentarlo.": dict(en="The file could not be prepared. Reload the page to try again.", fr="Le fichier n'a pas pu être préparé. Rechargez la page pour réessayer.", pt="Não foi possível preparar o ficheiro. Recarregue a página para tentar de novo.", de="Die Datei konnte nicht erstellt werden. Lade die Seite neu, um es noch einmal zu versuchen.", it="Non è stato possibile preparare il file. Ricarica la pagina per riprovare."),
"Para entrenadores de balonmano, baloncesto y fútbol que quieren organizar la temporada y registrar la carga de sus jugadores.": dict(
    en="For handball, basketball and football coaches who want to organise the season and record their players' load.",
    fr="Pour les entraîneurs de handball, de basket-ball et de football qui veulent organiser la saison et enregistrer la charge de leurs joueurs.",
    pt="Para treinadores de andebol, basquetebol e futebol que querem organizar a época e registar a carga dos seus jogadores.",
    de="Für Handball-, Basketball- und Fußballtrainer, die die Saison organisieren und die Belastung ihrer Spieler erfassen wollen.",
    it="Per allenatori di pallamano, pallacanestro e calcio che vogliono organizzare la stagione e registrare il carico dei loro giocatori."),
"Planifica con criterio. Entrena con datos.": dict(en="Plan with judgement. Train with data.", fr="Planifiez avec méthode. Entraînez avec des données.", pt="Planeie com critério. Treine com dados.", de="Mit Plan planen. Mit Daten trainieren.", it="Pianifica con criterio. Allena con i dati."),
"Planifícalo en ProTeam": dict(en="Plan it in ProTeam", fr="Planifiez-le dans ProTeam", pt="Planeie-o na ProTeam", de="Plane es in ProTeam", it="Pianificalo in ProTeam"),
"Plantilla gratis de planificación de temporada y control de carga (Excel)": dict(en="Free season planning and load control template (Excel)", fr="Modèle gratuit de planification de saison et de contrôle de la charge (Excel)", pt="Modelo grátis de planeamento da época e controlo de carga (Excel)", de="Kostenlose Vorlage für Saisonplanung und Belastungssteuerung (Excel)", it="Modello gratuito di pianificazione della stagione e controllo del carico (Excel)"),
"Plantilla gratis de planificación de temporada y control de carga (Excel) | ProTeam App": dict(en="Free season planning and load control template (Excel) | ProTeam App", fr="Modèle gratuit de planification de saison et de contrôle de la charge (Excel) | ProTeam App", pt="Modelo grátis de planeamento da época e controlo de carga (Excel) | ProTeam App", de="Kostenlose Vorlage für Saisonplanung und Belastungssteuerung (Excel) | ProTeam App", it="Modello gratuito di pianificazione della stagione e controllo del carico (Excel) | ProTeam App"),
"Probar ProTeam: primer equipo 3 meses gratis": dict(en="Try ProTeam: first team free for 3 months", fr="Essayer ProTeam : première équipe gratuite pendant 3 mois", pt="Experimentar a ProTeam: primeira equipa 3 meses grátis", de="ProTeam testen: erstes Team 3 Monate gratis", it="Prova ProTeam: prima squadra gratis per 3 mesi"),
"ProTeam App · Biblioteca": dict(en="ProTeam App · Library", fr="ProTeam App · Bibliothèque", pt="ProTeam App · Biblioteca", de="ProTeam App · Bibliothek", it="ProTeam App · Biblioteca"),
"ProTeam App · Recurso gratuito": dict(en="ProTeam App · Free resource", fr="ProTeam App · Ressource gratuite", pt="ProTeam App · Recurso gratuito", de="ProTeam App · Kostenlose Ressource", it="ProTeam App · Risorsa gratuita"),
"Recibe tu plantilla gratis": dict(en="Get your free template", fr="Recevez votre modèle gratuit", pt="Receba o seu modelo grátis", de="Hol dir deine kostenlose Vorlage", it="Ricevi il tuo modello gratuito"),
"Rondo 4x2 con transición": dict(en="4v2 rondo with transition", fr="Rondo 4x2 avec transition", pt="Rondo 4x2 com transição", de="Rondo 4-gegen-2 mit Umschalten", it="Torello 4 contro 2 con transizione"),
"Rueda de tiro con fatiga": dict(en="Shooting rotation under fatigue", fr="Rotation de tirs avec fatigue", pt="Roda de remate com fadiga", de="Wurfrotation unter Ermüdung", it="Ruota di tiro con fatica"),
"Tus datos se han guardado": dict(en="Your details have been saved", fr="Vos données ont été enregistrées", pt="Os seus dados foram guardados", de="Deine Daten wurden gespeichert", it="I tuoi dati sono stati salvati"),
"Una temporada, cinco hojas": dict(en="One season, five sheets", fr="Une saison, cinq feuilles", pt="Uma época, cinco folhas", de="Eine Saison, fünf Tabellenblätter", it="Una stagione, cinque fogli"),
"Ver ejercicio →": dict(en="View exercise →", fr="Voir l'exercice →", pt="Ver exercício →", de="Übung ansehen →", it="Vedi esercizio →"),
"Volver a descargar": dict(en="Download again", fr="Télécharger à nouveau", pt="Descarregar novamente", de="Erneut herunterladen", it="Scarica di nuovo"),
}

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
total = 0
for lang in ("en", "fr", "pt", "de", "it"):
    p = root / "src/lib/i18n/dict" / f"{lang}.json"
    raw = p.read_text(encoding="utf-8")
    d = json.loads(raw)
    n = 0
    for key, tr in T.items():
        if key not in d:
            sys.exit(f"{lang}: falta la clave {key!r}; el diccionario ha cambiado, revisar a mano")
        if d[key] == key and tr[lang] != key:
            d[key] = tr[lang]
            n += 1
    out = json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else "")
    p.write_text(out, encoding="utf-8")
    print(f"{lang}: {n} textos traducidos")
    total += n
print(f"Total: {total}")
