conf?=iachec

all: conference_data_$(conf).yaml form_map.yaml
	python fill_form.py -i Form_reimbursement.pdf -o form_filled_$(conf).pdf -d conference_data_$(conf).yaml -s 2 #-l

