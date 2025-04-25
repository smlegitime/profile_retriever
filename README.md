# Profile Retriever
Repository for retrieving LinkedIn profile information given someone's full name.

---

## About
The repository currently has an API structure (to be consumed by labeler), but contains a jupyter notebook for exploration (see `profile_retriever/notebooks/`).

### Folder Structure
```
└── 📁profile_retriever
    └── 📁notebooks
        └── profile.ipynb
        └── session.pkl
    └── 📁src
        └── 📁config
            └── config.py
            └── dev_config.py
            └── production_config.py
        └── 📁controllers
            └── __init__.py
            └── 📁__pycache__
                └── __init__.cpython-311.pyc
                └── profile_controller.cpython-311.pyc
            └── profile_controller.py
        └── routes.py
        └── utils.py
    └── 📁venv
    └── .env
    └── .gitignore
    └── app.py
    └── Dockerfile
    └── init_setup.py
    └── init_setup.sh
    └── README.md
    └── requirements.txt
    └── session.pkl
    └── template.py
    └── test.json
```