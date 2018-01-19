all: conference_data.yaml form_map.yaml
	python fill_form.py -i Form_reimbursement.pdf -o form_filled.pdf -d conference_data.yaml -s 2

