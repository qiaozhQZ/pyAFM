class BKT:
    def __init__(self, p_know, p_learn, p_guess, p_slip):

        self.p_learn = p_learn
        self.p_guess = p_guess
        self.p_slip = p_slip
        self.mastery_prob = p_know

    def update(self, correct):

        if correct:
            p_know_given_obs = ((self.mastery_prob * (1 - self.p_slip)) /
                    (self.mastery_prob * (1 - self.p_slip) + (1 - self.mastery_prob) * self.p_guess))

        else:
            p_know_given_obs = ((self.mastery_prob * self.p_slip) /
                    (self.mastery_prob * (self.p_slip) + (1 - self.mastery_prob) * (1 - self.p_guess)))
            
        # Probability not yet learned is proportional to not learning it now and having not learned previously
        self.mastery_prob = p_know_given_obs + (1 - p_know_given_obs) * self.p_learn

    def p_next_correct(self):

        return self.mastery_prob * (1 - self.p_slip) + (1 - self.mastery_prob) * self.p_guess


if __name__ == "__main__":

    bkt = BKT(p_know = 0.0000002966,
              p_learn = 0.1338697738,
              p_guess = 0.0760053940,
              p_slip = 0.1729474444)

    print('initial', bkt.mastery_prob)

    bkt.update(False)
    print('incorrect', bkt.p_next_correct())

    bkt.update(False)
    print('incorrect', bkt.p_next_correct())

    bkt.update(False)
    print('incorrect', bkt.p_next_correct())

    bkt.update(False)
    print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(True)
    # print('correct', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(True)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('correct', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('incorrect', bkt.p_next_correct())

    # bkt.update(False)
    # print('correct', bkt.p_next_correct())

    # bkt.update(True)
    # print('correct', bkt.p_next_correct())

    # bkt.update(False)
    # print('correct', bkt.p_next_correct())

    # bkt.update(False)
    # print('correct', bkt.p_next_correct())

    # bkt.update(True)
    # print('correct', bkt.p_next_correct())