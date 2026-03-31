import streamlit as st

st.title("🎶 Chor-Finanzplanung")

st.markdown("Berechnungsmodell, unter welchen Umständen sich der Chor finanziell trägt.")

# ---------------------------
# Eingaben
# ---------------------------
st.header("Eingaben")

members = st.number_input("Anzahl regelmäßig zahlender Mitglieder", min_value=0, value=18)
fee = st.number_input("Monatsbeitrag pro Person (€)", min_value=0.0, value=20.0)

choir_leader_1 = st.number_input("Kosten Gulia (€ / Monat)", min_value=0.0, value=250.0)
choir_leader_2 = st.number_input("Kosten Clara (€ / Monat)", min_value=0.0, value=0.0)

room_cost = st.number_input("Raumkosten (€ / Monat)", min_value=0.0, value=0.0)

# ---------------------------
# Berechnungen
# ---------------------------
revenue = members * fee
total_costs = choir_leader_1 + choir_leader_2 + room_cost
profit = revenue - total_costs

# Break-even Mitglieder
if fee > 0:
    break_even_members = total_costs / fee
else:
    break_even_members = 0

# ---------------------------
# Ergebnisse
# ---------------------------
st.header("Ergebnisse")

if profit >= 0:
    st.success("✅ Unser Chor ist finanziell tragfähig!")
else:
    st.error("❌ Wir machen Verlust.")

st.write(f"Wir benötigen mindestens **{break_even_members:.1f} Mitglieder**, um die Kosten zu decken.")

if room_cost > 0:
    st.write("-> Raumkosten sind berücksichtigt (z.B. näherer Proberaum).")

if choir_leader_2 > 0:
    st.write("-> Clara ist als zweite Chorleitung eingeplant.")

if profit < 0:
    st.write("-> Optionen:")
    st.write("- Beiträge erhöhen")
    st.write("- Mehr Mitglieder gewinnen")
    st.write("- Kosten reduzieren")

# ---------------------------
# Szenario-Hinweise
# ---------------------------
st.header("Berechnungsdetails")

st.write(f"**Einnahmen:** {revenue:.2f} €")
st.write(f"**Kosten:** {total_costs:.2f} €")
st.write(f"**Ergebnis:** {profit:.2f} €")
