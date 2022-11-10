import dagstermill as dm

from dagster import job

k_means_iris = dm.define_dagstermill_op(
    "k_means_iris",
    #script_relative_path("ml_insanity.ipynb"),
    notebook_path = "notebooks/ml_insanity.ipynb",
    output_notebook_name="iris_kmeans_output",
)


@job(
    resource_defs={
        "output_notebook_io_manager": dm.local_output_notebook_io_manager,
    }
)
def iris_classify():
    k_means_iris()

