from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ffms_secret"

# In-memory data store
data = {
    "ingredients": [],
    "batches": [],
    "users": [
        {"username": "admin", "password": "admin123", "role": "Admin"},
        {"username": "inventory", "password": "inv123", "role": "Inventory Supervisor"},
        {"username": "production", "password": "prod123", "role": "Production Manager"},
        {"username": "inspector", "password": "qc123", "role": "Quality Inspector"},
        {"username": "shipping", "password": "ship123", "role": "Shipping Clerk"},
    ],
    "logs": []
}

def log(msg):
    data["logs"].append({"time": datetime.now().strftime("%H:%M"), "msg": msg})

# ── Auth ──────────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = next((u for u in data["users"] if u["username"] == username and u["password"] == password), None)
        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            log(f"User login: {username}")
            return redirect(url_for("inventory"))
        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ── Inventory ─────────────────────────────────────────────
from datetime import datetime, date

@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        ingredient = {
            "id": len(data["ingredients"]) + 1,
            "name": request.form["name"],
            "quantity": int(request.form["quantity"]),
            "unit": request.form["unit"],
            "expiry": request.form["expiry"],
            "batch_no": f"ING-{len(data['ingredients'])+1:03d}"
        }
        data["ingredients"].append(ingredient)
        log(f"Ingredient added: {ingredient['name']}")
        return redirect(url_for("inventory"))

    # Calculate days left for each ingredient
    today = date.today()
    ingredients_with_days = []
    near_expiry = []

    for i in data["ingredients"]:
        expiry_date = datetime.strptime(i["expiry"], "%Y-%m-%d").date()
        days_left = (expiry_date - today).days
        i_copy = dict(i)
        i_copy["days_left"] = days_left
        ingredients_with_days.append(i_copy)
        if days_left <= 30:   # only show if expiring within 30 days
            near_expiry.append(i_copy)

    return render_template("inventory.html",
                           ingredients=ingredients_with_days,
                           near_expiry=near_expiry,
                           role=session.get("role"))

# ── Production ────────────────────────────────────────────
@app.route("/production", methods=["GET", "POST"])
def production():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        if not data["ingredients"]:
            flash("Cannot create batch: no ingredients in inventory!")
            return redirect(url_for("production"))
        batch = {
            "id": len(data["batches"]) + 1,
            "batch_no": f"BTH-{len(data['batches'])+1:03d}",
            "product": request.form["product"],
            "quantity": request.form["quantity"],
            "ingredients_used": request.form["ingredients"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": "In Progress"
        }
        data["batches"].append(batch)
        log(f"Batch created: {batch['batch_no']} - {batch['product']}")
        return redirect(url_for("production"))
    return render_template("production.html", batches=data["batches"],
                           ingredients=data["ingredients"], role=session.get("role"))

# ── Quality Inspection ────────────────────────────────────
@app.route("/inspection", methods=["GET"])
def inspection():
    if "user" not in session:
        return redirect(url_for("login"))
    pending = [b for b in data["batches"] if b["status"] == "In Progress"]
    return render_template("inspection.html", batches=pending, role=session.get("role"))

@app.route("/inspect/<int:batch_id>/<action>")
def inspect(batch_id, action):
    batch = next((b for b in data["batches"] if b["id"] == batch_id), None)
    if batch:
        batch["status"] = "Approved" if action == "approve" else "Rejected"
        log(f"Batch {batch['batch_no']} {batch['status']}")
    return redirect(url_for("inspection"))

# ── Shipping ──────────────────────────────────────────────
@app.route("/shipping", methods=["GET"])
def shipping():
    if "user" not in session:
        return redirect(url_for("login"))
    approved = [b for b in data["batches"] if b["status"] == "Approved"]
    dispatched = [b for b in data["batches"] if b["status"] == "Dispatched"]
    return render_template("shipping.html", approved=approved, dispatched=dispatched, role=session.get("role"))

@app.route("/dispatch/<int:batch_id>")
def dispatch(batch_id):
    batch = next((b for b in data["batches"] if b["id"] == batch_id), None)
    if batch and batch["status"] == "Approved":
        batch["status"] = "Dispatched"
        log(f"Batch {batch['batch_no']} dispatched")
    return redirect(url_for("shipping"))

# ── Admin ─────────────────────────────────────────────────
@app.route("/admin")
def admin():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("admin.html", users=data["users"], logs=data["logs"],
                           batches=data["batches"], ingredients=data["ingredients"],
                           role=session.get("role"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)