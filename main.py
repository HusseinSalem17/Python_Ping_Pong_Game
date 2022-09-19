# اول حاجه للازم اعمل import لمكتبه turtle عشان بتساعدني اني ارسم اشكال علي بايثون اوخليها تتحرك
import turtle

# اجي الوقت الي اعمل فيه الشاشه الي اللعبه بتاعتي هتشتغل جواها
# هستدعي داله Screen من داخل كلاس ال turtle عشان الداله دي بتنشألي الشاشه الي هشوف جواها اللعبه
wind = turtle.Screen()
#  محتاج احط عنوان لل screen الي هعملها ودا عن طريق المتغير الي انشات جواه ال Screen Object واستدعي داله title
wind.title("Ping Pong By Hussein")
# ابدا بقي اظبط الشاشه من حيث الطول والعرض بتاعها ولونها كمان
wind.bgcolor("black")  # كدا انا حددت اللون الخلفيه بتاع الشاشه
wind.setup(width=800, height=600)  # دي بقي عشان احدد الطول والعرض بتاع الشاشه
wind.tracer(
    0)  # داله  tracer دي مهمه جدا ودا انها تمنع ال Screen انها تعمل تحديث لنفسها
# ودا بيديني الافضليه في التحكم في سرعه تحديث الشاشه ودا ميزته اني اعرف اسرع اللعبه زي ما انا عايز
# وبكدا انا خلصت اعدادات الشاشه الي يظهر فيها نتيجه كل الكود الي يظهر فيها اللعبه بعد كدا
# الوقتي بقي محتاج اعمل الحلقه التكراريه بتاعت اللعبه الي اسمها game loop  فدا موجود فاي لعبه عشان دي الي بتخلي اللعبه لسه شغاله
#   فعشان نعمل كدا هنكتب الي تحت دا

# الوقتي انا محتاج تلات حاجات اعملهم هما مضربين وكوره

# madrab 1

# المضرب هيبقي عباره عن Turtle object ومن خلال ال object دا اعمل شكل المضرب زي ما انا عايزه
madrab1 = turtle.Turtle()
# تاني حاجه محتاج اظبط سرعه ال animation بتاعت المضرب دي مش سرعه حركه المضرب لا دي سرعه رسم المضرب علي الشاشه كل ما يتحرك عشان اقدر اشوفه
# صفر في داله speed دي معناها اني عايز اعمل شكل المضرب يترسم علي الشاشه باعلي سرعه عشان لو معملتش كدا هحس ان المضرب بيعلق لما اللعبه تتحرك
madrab1.speed(0)
# تالت حاجه محتاج احدد شكل المضرب وفي شويه اشكال جاهزه جوا ال Turtle module فهستخدم منهم شكل المربع
# داله shape اقدر من خلالها احدد الشكل فهستخدم شكل المربع عشان كدا هكتب فيها square
madrab1.shape("square")
# رابع حاجه عايز احدد لون المضرب
madrab1.color("blue")
# بعد كدا محتاج انده علي داله مهمه هي penup عشان object Turtle بطبيعته لما بتمشي
# علي الشاشه بيبقي في وراها خطوط وانا مش عايز يبقي في اي خطوط وراها عشان كدا بنادي علي الداله penup الي تمنع ال object Turtle ترسم اي خطوط
madrab1.penup()
# الوقتي بقي محتاج احدد المضرب يظهر في انهي حته في الشاشه
# وانا بتعامل مع الشاشه علي انها محاور x & y والطول 600 ينفسم ال 300 & -300 والعرض 800 ينفسم ل 400 & -400 وانا عايز اول مضرب يظهر علي اقصي
# الشمال من الشاشه يبقي اقصي الشمال هو -400 فعشان كمان احطه في اقصي الشمال بس ميكونش لازق اوي في الطرف فمش هكتب بالضبط -400 فمثلا هكتبها -350
# عشان اكتب الداله الي تحدد المضرب يظهر فين عن طريق دالهه goto واكتب فيها احداثيات x & y
madrab1.goto(-350, 0)
# حجمه تلقائي ال هو 20px for width & 20px height بيبقي مش كبير فلازم اظبط حجمه انا بقي عن طريق داله shapesize فانا عايز اول طول المضرب عشان يبقي طويل شويه
# الي بيحصل في الداله انه بعمل stretch الطول والعرض علي حسب الرقم الي انا بدخله في داله
# shapesize فالي انا كتبته 5 فدا همط الطول بعامل 5 يعني 5 *20px تبقي 100px وال 1 *20px تبقي 20px زي ما هي يبقي كدا الطول 100px والعرض ب 20px زي ما هو
# خلي بالك انا كاتب مط العرض لان الشاشه بتبقي landscape مثلا فالعرض بتاع المضرب هو الطول لما يبقي landscape عشان لما امط العرض تبقي طولت فدا الشرح
madrab1.shapesize(stretch_wid=5, stretch_len=1)

# madrab 2

madrab2 = turtle.Turtle()  # initializes turtle object( shape )
madrab2.speed(0)  # set the speed of the animation
madrab2.shape("square")  # set the shape of the object
madrab2.color("red")  # set the color of the shape
madrab2.penup()  # stops the object from drawing lines
madrab2.goto(350, 0)  # set the position of the object
madrab2.shapesize(stretch_wid=5, stretch_len=1)  # stretches ths shape to meet the size

# ball

# الكوره بقي مش عايز امطها لا عايز زي ما هي حجمها صغير
# وكمان محتاج اغير مكان الكوره واخليها في النص بقي
# وكمان اخلي شكلها دائره بدل مربع
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# الي محتاج اعمله الوقتي اني اخلي الكوره تتحرك علشاشه ان الكوره لما تخبط فوق ولا تحت ترد تاني في الاتجاه المعاكس ولما  تطلع
# برا حدود الشاشه سواء علي اليمين او علي الشمال ترجع الكوره تاني في النص وتبدا تتحرك في الاتجاه
# المعاكس عشان نعمل كدا عايزين نفرق بين حاجتين هي تحريك الكره هلي x-axis وتحريك الكره علي y-axis
# حرف d معناه delta يرمز لمعامل التغير و x for x -axis & y for y-axis
# الي تحت دا معناه ان كل مره الكوره تتحرك فيها عايز x & y يزيدوا ب 2.5px علي الشاشه بما ان 2.5 في dx & dy موجب فمعناه ان كدا هتحرك يمين وفوق
ball.dx = 0.2
ball.dy = 0.2

# score
# هنعمل دا بردوا باستخدام ال turtle module
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)  # دي سرعه التحرك يعني سرعه رسم البيكسلز علي الشاشه
score.color("white")
score.penup()
score.hideturtle()  # دي عشان مش عايز اشوف الشكل بتاع ال object عايز بس اشوف ال text الي هيكتب من خلال ال object دا الي هيعرضلي ال score بتاع اللغيبه
score.goto(0, 260)  # احدد مكان الي يطلع فيه ال score
score.write("Player 1: 0 || Player 2: 0", align="center",
            font=("Courier", 24, "normal"))  # عشان اكتب ال text  الي هيطلع


# functions

# الدوال دي هي الي هتحدد اللعبه دي هتشتغل ازاي
# فانا الوقتي هعمل داله تخليني احرك المضارب بتاعتي فوق وتحت
# فاول داله هو داله التحكم في المدرب الاولاني ويخليني اعرف احركه لفوق
# عشان اصلا احرك المضرب لازم اكون عارف مكانه فين عشان اعرف اغير مكانه واتحرك فيه
# وبما اني بحرك المضرب بتاعي لفوق وتحت فالحاجه الي محتاج اعرفها هي تحركه بالنسبه لمحور الصادات
#   تحركات المضرب الاول
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)  # كدا اما الداله دي استدعيها هتحرك المضرب من مكانه ل 20 زياده لفوق
    # داله ycor هي داله في Turtle module بيجبلي مكان ال y بتاع ال object الي ندهت عليه
    # فلما انا ندتها من خلال madrab1 هيجبلي مكان المضرب الاول علي الشاشه من حيث محور الصادات
    # دلوقتي انا عايز اتحرك لفوق معناها عايز ازود قيمه ال y
    # كدا كل مره اتحرك فوق هزود 20px والسطر دا خلاني احدد ال ycor
    # الجديده يعني قيمتها هتبقي القيمه الي راجعه في y من داله ycor زائد 20 الجديده بتاعت التحرك
    # الوقتي محتاج اقول للمضرب ان ال y الجديده دي هي المفروض تتحط عنده مكان ال y القديمه الي عنده عشان كدا عملت الداله الي تحت


def madrab1_down():
    y = madrab1.ycor()  # get the y coordinate of the madrab1
    y -= 20  # set the  y to increase be 20
    madrab1.sety(y)  # set the y of the madrab1 to the new coordinate


#   تحركات المضرب الثاني
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard bindings

# دي عشان نربط زراير الكيبورد بالدوال الي هعملها عشان نعرف من خلال الزراير دي نشغل الداله وننده عليها وفعلا المضرب يبتدي يتحرك
# عشان كدا كتبت اسم ال object بتاع الشاشه بتاعتنا واستدعي داله Listen عشان دي بتعرف الشاشه ان في احتمال ان زراير علي الكيبورد تداس وتستني تشوف اي الزراير الي هتداس
wind.listen()  # السطر دا بيعرف الشاشه ان في زراير هتداس
# السطر الي تحت بقي دا بقي بيقول انه لما يداس علي زرار ال w انده علي داله madrab1_up وخلي بالك لازم ال w is lowerCase
#   زراير تحرك المضرب 1
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
#   زراير تحرك المضرب 2
wind.onkeypress(madrab2_up, "Up")  # كلمه Up يعني السهم لاعلي الي في الكيبورد
wind.onkeypress(madrab2_down, "Down")  # كلمه Down معناها السهم لاسفل الي فالكيبورد

# main game loop
while True:
    # انادي علي داله update يعني الداله دي فكل مره اللوب هيشتغل الشاشه هتحدث
    # نفسها ودا انا محتاج اعمله عشان الداله الي فوق الي اسمها tracer الي اخد قيمه 0 دا بيخليني اني اوقف ان اللعبه تتحدث بشكل تلقائي
    # وبيخليني انا اتحكم في التحديث ودا انا عملته من خلال داله ال update الي بيخليني احدث الشاشه بعد نا كل الكود الي في while loop يكون اتنفذ
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball starts at 0 and everytime loops run -->+2 x-axis
    ball.sety(ball.ycor() + ball.dy)  # ball starts at 0 and everytime loops run -->+2 y-axis

    # الي محتاج اعمله ان الكوره لما تخبط في الحدود سواء فوق او تحت ترد في الاتجاه المعاكس متطلعش برا الشاشه

    # border check
    # top border +300px, bottom border -300px, ball is 20px
    # تظبيط من فوق وتحت
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction , making +2.5 --> -2.5

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)  # set y coordinate -290
        ball.dy *= -1  # reverse direction , making -2.5 --> +2.5

    # تظبيط من اليمين والشمال
    if ball.xcor() > 390:  # if ball is at right border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse the x direction
        score1 += 1
        score.clear()  # الداله دي بتمسح اي text موجود قبل كدا عشان يتحط ال score الجديد والقديم يكون اتمسح
        score.write("Player 1: {} || Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))  # عشان اكتب ال text  الي هيطلع

    if ball.xcor() < -390:  # if ball is at left border
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse the x direction
        score2 += 1
        score.clear()
        score.write("Player 1: {} || Player 2: {}".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))  # عشان اكتب ال text  الي هيطلع

    # الوقتي عايز الكوره ترد في الاتجاه المعاكس لما تخبط في المضارب
    # عشان نعمل كدا لازم نقارن بين ال x & y بتوع الكوره وال x & y بتوع المضارب زي ما عملنا فوق لما
    # قارنا ال x & y بتوع الكوره مع ال x & y بتوع الشاشه من عند اطراف الشاشه
    # لو طلعنا فوق لما جينا نحط اماكن المضارب هنلاقي في madrab2 حطناه عند +350 الخاص ب x-axis يعني x coordinate الي هو
    # يعني نص المضرب التاني مكانها عند 350 وعرض المضرب كان 20px والطول 100px فعشان اشوف الكوره خبطت
    # ولا لا عايز اشوف ما بين حدود المضرب الي هو طوله 100px وهل لمست ما بين طرف المضرب لنص المضرب عشان لما الكوره تلمسها ترد من المضرب

    # تصادم مضرب و الكوره
    # الزياده والنقص 40 عشان متفقين ان الكوره اصلا 20 فهي من فوق اصلا 10 ومن تحت 10 ودا كله موضح اكتر في الصوره
    # madrab2
    if (340 < ball.xcor() < 350) and (madrab2.ycor() + 40 > ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    # madrab1
    if (-340 > ball.xcor() > -350) and (madrab1.ycor() + 40 > ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

# الداله دي .format(score1,score2) الي بتعمله انها بتحط القيم الي فيها مكان الاقواس دي {}
