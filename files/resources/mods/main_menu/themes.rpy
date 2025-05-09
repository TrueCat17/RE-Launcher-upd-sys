init python:
	themes = {}
	
	def set_theme(name):
		if name not in themes and name not in user_themes:
			name = 'Day'
		
		global theme
		theme = (themes if name in themes else user_themes)[name]
		
		persistent.theme_name = name
		
		input.fog = im.rect(theme.input_fog_color)
		
		input.bg = im.round_rect(theme.back_bg_color, 100, 100, 12)
		input.bg_border_size = 0
		
		input.tf_bg        = im.round_rect(theme.panel_bg_color,     200, 20, 6)
		input.tf_bg_border = im.round_rect(theme.panel_border_color, 200, 20, 6)
		
		input.prompt_color = input.tf_color = theme.text_color
	
	
	day_theme = Object(
		back_bg_color = '#EEE',
		
		panel_border_color = '#BBB',
		panel_bg_color = '#E0E0E0',
		
		dotted_line_color = '#04B',
		
		text_font = 'Fregat_bold',
		text_color = '#04B',
		
		version_text_font = 'Fregat_bold',
		version_text_color = '#111',
		
		btn_text_font = 'Fregat_bold',
		btn_text_color = '#111',
		btn_text_color_hover = '#04B',
		btn_ground_color = '#00000002',
		btn_hover_color  = '#00000002',
		
		panel_btn_text_font = 'Fregat_bold',
		panel_btn_text_color = '#FFF',
		panel_btn_text_color_hover = '#000',
		panel_btn_ground_color = '#38E',
		panel_btn_hover_color  = '#47D877',
		
		new_btn_colors = ('#FF9948', '#D84'), # 2 colors of gradient
		doc_btn_colors = ('#44D474', '#3B5'),
		start_btn_colors = 'doc_btn_colors', # or prop name with real colors
		
		icon_ground_color = '#111',
		icon_hover_color = '#04B',
		
		open_text_font = 'Fregat_bold',
		open_text_color = '#111',
		open_text_color_inactive = '#777',
		
		open_btn_text_font = 'Fregat_bold',
		open_btn_text_color = '#111',
		open_btn_text_color_hover = '#111',
		open_btn_ground_color = '#00000002',
		open_btn_hover_color  = '#888',
		
		input_fog_color = '#0006',
	)
	themes['Day'] = day_theme
	
	
	themes['Night'] = Object(day_theme,
		back_bg_color = '#202020',
		
		panel_border_color = '#3F3F3F',
		panel_bg_color = '#262626',
		
		dotted_line_color = '#7B7B7B',
		
		text_color = '#FFF',
		
		version_text_color = '#FFF',
		
		btn_text_color = '#7B7B7B',
		btn_text_color_hover = '#E9E9E9',
		
		panel_btn_text_color = '#ABABAB',
		panel_btn_text_color_hover = '#E9E9E9',
		panel_btn_ground_color = '#333',
		panel_btn_hover_color  = '#444',
		
		new_btn_colors = ('#99431A', '#D97A14'),
		doc_btn_colors = ('#292099', '#267CC7'),
		
		icon_ground_color = '#7B7B7B',
		icon_hover_color = '#FFF',
		
		open_text_color = '#7B7B7B',
		open_text_color_inactive = '#4B4B4B',
		
		open_btn_text_color = '#7B7B7B',
		open_btn_text_color_hover = '#FFF',
		open_btn_hover_color  = '#262626',
		
		input_fog_color = '#FFF5'
	)
	
	
	themes['Summer'] = Object(day_theme,
		back_bg_color = '#0A6',
		
		panel_border_color = '#FD0',
		panel_bg_color = '#084',
		
		dotted_line_color = '#FD0',
		
		text_color = '#EE0',
		
		btn_text_color = '#FF0',
		btn_text_color_hover = '#F80',
		
		panel_btn_hover_color = '#E82',
		
		new_btn_colors = ('#FA3', '#F71'),
		doc_btn_colors = ('#09F', '#06F'),
		
		icon_ground_color = '#FF0',
		icon_hover_color = '#111',
		
		open_text_color_inactive = '#050',
		
		open_btn_text_color = '#EE0',
		open_btn_text_color_hover = '#EE0',
		open_btn_hover_color = '#0A0',
		
		input_fog_color = '#0486',
	)
	
	
	themes['Light'] = Object(day_theme,
		back_bg_color = '#F8F8F8',
		
		panel_border_color = '#C4C4C4',
		panel_bg_color = '#FFF',
		
		dotted_line_color = '#9A9A9A',
		
		text_color = '#2E2B36',
		
		version_text_color = '#2E2B36',
		
		btn_text_color = '#999',
		btn_text_color_hover = '#2B2E36',
		
		panel_btn_text_color = '#595959',
		panel_btn_text_color_hover = '#FFF',
		panel_btn_ground_color = '#DDD',
		panel_btn_hover_color  = '#686868',
		
		new_btn_colors = ('#CA5E2A', '#FF9524'),
		doc_btn_colors = ('#4435FF', '#009BFA'),
		
		icon_ground_color = '#999',
		icon_hover_color = '#2B2E36',
		
		open_text_color = '#999',
		open_text_color_inactive = '#CECECE',
		
		open_btn_text_color = '#999',
		open_btn_text_color_hover = '#2B2E36',
	)
	
	
	themes['Contrast'] = Object(day_theme,
		back_bg_color = '#DDD',
		
		panel_border_color = '#111',
		panel_bg_color = '#AAA',
		
		dotted_line_color = '#111',
		
		text_color = '#00F',
		
		btn_ground_color = '#111',
		btn_hover_color  = '#EEE',
		btn_text_color = '#EEE',
		btn_text_color_hover = '#111',
		
		new_btn_colors = ('#A0F', '#80D'),
		doc_btn_colors = ('#E11', '#C11'),
		
		panel_btn_ground_color = '#111',
		panel_btn_hover_color  = '#EEE',
		
		icon_ground_color = '#EEE',
		icon_hover_color = '#111',
		
		input_fog_color = '#0009',
	)
	
	
	
	set_theme(persistent.theme_name)
