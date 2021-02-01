import os
import math
import cmath
import re
#from discord import File
#from matplotlib import pyplot as plt
import numpy as np
from discord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix = '$')

@bot.command()
async def inputRectangular(ctx, arg1, arg2):
  pattern = re.compile('\-?[0-9]+')
  x = re.match(pattern, arg1)
  y = re.match(pattern, arg2)
  if x and y:
    if get_mag(arg1, arg2) is not None:
      await ctx.send("Magnitude : {}".format(get_mag(arg1, arg2)))
      await ctx.send("Phase(radians) : {}".format(get_phase(arg1, arg2)))
      await ctx.send("Phase(degrees) : {}".format(np.rad2deg(get_phase(arg1, arg2))))
      await ctx.send("Polar (Radians): {}".format(get_polar(make_complex(arg1, arg2))))
    else:
      await ctx.send("Incorrect format. Send two numbers")
  else:
    await ctx.send("Incorrect format. Send two numbers")

@bot.command()
async def inputPol(ctx, arg1, arg2):
  pattern = re.compile('\-?[0-9]+')
  x = re.match(pattern, arg1)
  y = re.match(pattern, arg2)
  if x and y:
    if make_complex(arg1, arg2) is not None:
      await ctx.send("Rect : {}".format(get_rect(arg1, arg2)))
    else:
      await ctx.send("Incorrect format. Send two numbers")
  else:
    await ctx.send("Incorrect format. Send two numbers")


def make_complex(re, im):
  try:
    re = float(re)
    im = float(im)
  except:
    return None
  return complex(re, im)
def get_mag(re, im):
  try:
    re = float(re)
    im = float(im)
  except:
    return None
  return math.sqrt(re**2+im**2)
def get_phase(re, im):
  re = float(re)
  im = float(im)
  val = math.atan2(abs(im), abs(re))
  if (re >= 0 and im >= 0):
    return val
  elif (re < 0 and im>= 0):
    return math.pi-val
  elif (re < 0 and im < 0):
    return val-math.pi
  else: 
    return -1*val
def get_polar(x):
  return cmath.polar(x)
def get_rect(r, phi):
  r = float(r)
  phi = float(phi)
  return cmath.rect(r, phi)

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  print("Call $inputRectangular or $inputPol to input first and second number")

# @bot.command()
# async def graphRect(ctx, arg1, arg2):
#   pattern = re.compile('\-?[0-9]+')
#   x = re.match(pattern, arg1)
#   y = re.match(pattern, arg2)
#   if x and y:
#     try:
#       arg1 = float(arg1)
#       arg2 = float(arg2)
#     except:
#       await ctx.send("Error")
#     await ctx.send("Input is ok")
#     graph = File('graph.png')
#     ax = plt.axes()
#     ax.arrows(0, 0, arg1, arg2)
#     plt.savefig('graph.png')
#     await ctx.send(file=graph)
#   else:
#     await ctx.send("Incorrect format. Send two numbers")

keep_alive()

bot.run(os.getenv('TOKEN'))
