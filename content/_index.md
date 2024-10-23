---
####################### Banner #########################
banner:
  title : "The shiny title"
  content : "A suite of integrated Open Source projects to plan and document your next cloning project"

##################### Feature ##########################
feature:
  enable : true
  feature_item:
    # feature item loop
    - name : "pydna"
      icon : "fas fa-dna"
      content : "Python library to simulate cloning<br>(PCR, Gibson, Golden Gate...)"

    # feature item loop
    - name : "teemi"
      icon : "fas fa-bacterium"
      content : "Pydna extension for strain engineering<br>Jupyter Notebooks as experiment documentation"

    # feature item loop
    - name : "ShareYourCloning"
      icon : "fas fa-window-restore"
      content : "Web application to plan and visualize cloning strategies<br>No need to code!"

    # feature item loop
    - name : "Single data model"
      icon : "fas fa-database"
      content : "All tools produce and understand the same file format"



######################### Service #####################
service:
  enable : true
  service_item:
    # service item loop
    - title : "Pydna"
      scripts:
      - path: "./script1.py"
        title: "Design primers for Gibson Assembly"
      - path: "./script1.py"
        title: "Simulate restriction and ligation"
      - path: "./script1.py"
        title: "Another example"
      content : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat. consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat."
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/BjornFJohansson/pydna"
        
    # service item loop
    - title : "ShareYourCloning"
      images:
      - "images/service-2.png"
      - "images/service-2.png"
      content : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat. consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat."
      button:
        enable : true
        label : "Check it out"
        link : "https://shareyourcloning.org"

# service item loop
    - title : "Teemi"
      scripts:
      - path: "./script1.py"
        title: "Example 1"
      - path: "./script1.py"
        title: "Example 2"
      - path: "./script1.py"
        title: "Example 3"
      content : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat. consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat."
      button:
        enable : true
        label : "Check it out"
        link : "https://github.com/hiyama341/teemi"

        
    # service item loop
    - title : "Single data model"
      images:
      - "images/service-2.png"
      content : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat. consectetur adipiscing elit. Consequat tristique eget amet, tempus eu at consecttur. Leo facilisi nunc viverra tellus. Ac laoreet sit vel consquat."
      button:
        enable : true
        label : "Check it out"
        link : "/about/"
        

#################### Logo section #####################
logo:
  enable : true
  logo_items:
    - image: "https://www.pombase.org/assets/pombase-logo.png"
      link: "https://www.pombase.org"
    - image: "https://www.shareyourgreendesign.com/wp-content/uploads/2023/12/opp_3210.png"
      link: "https://www.dtu.dk/english/"
    - image: "https://www.elabftw.net/img/elabftw-logo.png"
      link: "https://www.elabftw.net/"
    - image: "https://www.embl.org/guidelines/design/wp-content/uploads/2022/02/EMBL_logo_colour_DIGITAL.png"
      link: "https://labid-demo.embl.de/"


##################### Call to action #####################
call_to_action:
  enable : true
  title : "Join our community"
  image : "images/cta.svg"
  content : "Partner with like-minded scientists to improve documentation and reproducibility in cloning"
  button:
    enable : true
    label : "Contact Us"
    link : "contact/"
---
