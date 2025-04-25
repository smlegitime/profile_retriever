# Profile Retriever
Repository for retrieving LinkedIn profile information given someone's full name.

---

## About
The repository currently has an API structure (to be consumed by labeler), but contains a jupyter notebook for exploration (see `profile_retriever/notebooks/`).

### Folder Structure
```
└── 📁profile_retriever
    └── 📁methods
        └── scraping_methods.md
    └── 📁notebooks
        └── profile.ipynb
    └── 📁src
        └── 📁config
            └── config.py
            └── dev_config.py
            └── production_config.py
        └── 📁controllers
            └── profile_controller.py
        └── routes.py
        └── utils.py
    └── 📁test
        └── name_to_company_proxycurl.csv
        └── name_to_company.csv
        └── scrapingbee_res.json
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
```