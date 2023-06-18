# api-poc

python3 -m venv myenv

virtualenv myenv

Replace myenv with the desired name for your virtual environment.

Once the virtual environment is created, activate it:

source myenv/bin/activate
myenv\Scripts\activate

To install packages in the virtual environment, use the pip command:
pip install package_name

When you are done working with the virtual environment, you can deactivate it:

deactivate


gcloud projects add-iam-policy-binding tatami-devops --member=user:rodolfocasanova.dev@gmail.com --role=roles/container.clusterViewer

gcloud container clusters get-credentials --project=tatami-devops --region=us-central1-c gke-terraform-learn
