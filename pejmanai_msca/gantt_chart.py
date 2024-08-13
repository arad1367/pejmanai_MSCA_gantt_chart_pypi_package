import plotly.figure_factory as ff
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.io as pio
import kaleido

def get_last_day_of_month(year, month):
    """Returns the last day of the given month and year."""
    if month == 12:
        return datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        return datetime(year, month + 1, 1) - timedelta(days=1)

def create_gantt_chart(work_packages, milestone_color, deliverable_color, annotation_text, start_date, finish_date, project_title, save=False):
    """
    Create a Gantt chart from work packages with custom colors and annotations.

    Parameters:
    - work_packages: List of dictionaries, each representing a task with 'Task', 'Start', 'Finish', and 'Type'.
    - milestone_color: Color code for milestones.
    - deliverable_color: Color code for deliverables.
    - annotation_text: Text for the annotation explaining work packages.
    - start_date: Start date for the x-axis in 'YYYY-MM-DD' format.
    - finish_date: Finish date for the x-axis in 'YYYY-MM-DD' format.
    - project_title: Title of the project to be displayed at the top of the chart.
    - save: Boolean, if True, the chart is saved as a high-quality PNG file.

    Returns:
    - None: Displays the Gantt chart.
    """

    # Convert Start and Finish to datetime objects
    for task in work_packages:
        task["Start"] = datetime.strptime(task["Start"], "%Y-%m-%d")
        task["Finish"] = datetime.strptime(task["Finish"], "%Y-%m-%d")

    # Convert start_date and finish_date to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    finish_date = datetime.strptime(finish_date, "%Y-%m-%d")

    # Create a list of the last day of each month between start_date and finish_date
    current_date = start_date
    last_days = []
    while current_date <= finish_date:
        last_day = get_last_day_of_month(current_date.year, current_date.month)
        if last_day >= start_date:
            last_days.append(last_day)
        current_date = last_day + timedelta(days=1)

    # Generate tick text for each of the last days
    tick_vals = last_days
    tick_text = [date.strftime('%d/%m/%Y<br><b>%B %Y</b>') for date in last_days]

    # Create the Gantt chart
    fig = ff.create_gantt(
        work_packages,
        index_col='Type',
        colors={task["Type"]: milestone_color if task["Type"].startswith("M") else deliverable_color for task in work_packages},
        group_tasks=True,
        showgrid_x=True,
        showgrid_y=True,
        title=project_title,  # Set the project title as the chart title
        show_colorbar=False,
        show_hover_fill=False  # Display task name as hover text
    )

    # Add dummy traces for the legend
    fig.add_trace(go.Bar(
        x=[None],
        y=[None],
        marker=dict(color=milestone_color),
        name="Milestones",
        orientation='h',
        showlegend=True
    ))

    fig.add_trace(go.Bar(
        x=[None],
        y=[None],
        marker=dict(color=deliverable_color),
        name="Deliverables",
        orientation='h',
        showlegend=True
    ))

    # Update layout for legend, x-axis, and y-axis
    fig.update_layout(
        legend_title="Task Types",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,  # Adjust the y-position of the legend
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            title="Timeline",
            tickformat="%d/%m/%Y",
            tickvals=tick_vals,
            ticktext=tick_text,
            tickangle=-70,  # Rotate tick labels for better readability
            ticks="outside",
            tickmode="array",
            range=[start_date, finish_date],
            showgrid=True
        ),
        yaxis_title="Work packages (WPs) and tasks",
        title_x=0.5
    )

    # Add annotations for work package explanations
    annotations = [
        go.layout.Annotation(
            text=f"<b>Work Package Explanations</b><br>{annotation_text}",
            align="left",
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0.99,  # Adjust the x-position of the annotation
            y=1.00,  # Adjust the y-position of the annotation
            bordercolor="black",
            borderwidth=1,
            font=dict(size=12)
        )
    ]

    fig.update_layout(annotations=annotations)

    # Show the figure
    fig.show()