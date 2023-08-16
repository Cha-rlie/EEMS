# Import the necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

# Import the necessary custom libraries
import simulation

class simulation_handler:

    def __init__(self):
    # Start the simulation
        self.simulation = simulation.Simulation()

        self.simulation.run_round()

        Writer = animation.writers["ffmpeg"]
        writer = Writer(fps=20, metadata=dict(artist="Me"), bitrate=1800)

    def history_of_each_sectors_money_lineplot(self):
        fig = plt.figure(figsize=(10, 6))

        sns.set_style("darkgrid")
        plt.title("History of Each Sector's Money")
        plt.xlabel("Round")
        plt.ylabel("Money")
        # plt.yscale('log')


        def animate(i):
            self.simulation.run_round()
            p = sns.lineplot(self.simulation.money_of_all_sectors_db)
            plt.legend(self.simulation.money_of_all_sectors_db.columns)


        ani = animation.FuncAnimation(fig, animate, interval=1000)

        plt.show()

    def percentage_ownership_of_circulating_money_piechart(self):
        fig = plt.figure(figsize=(10, 6))

        plt.title("Sector's Ownership Over the Total Positive Circulating Money")
        # define Seaborn color palette to use
        palette_color = sns.color_palette('pastel')

        def animate(i):
            self.simulation.run_round()
            p = plt.pie(self.simulation.percentage_ownership_db.loc[len(self.simulation.percentage_ownership_db)-1], colors=palette_color)
            plt.legend(self.simulation.percentage_ownership_db.columns)


        ani = animation.FuncAnimation(fig, animate, interval=1000)

        plt.show()

#simulation_handler = simulation_handler()
#simulation_handler.percentage_ownership_of_circulating_money_piechart()